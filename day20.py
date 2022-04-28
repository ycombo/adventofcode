import math
import re
from functools import reduce
from operator import mul

import utils


def parse_img(img_part: str):
    lines = img_part.splitlines()
    return (utils.ints(lines[0])[0], lines[1:])

all_pics = utils.get_list_data_from_file('day20.txt', parser=parse_img, sep='\n\n')

MONSTER= [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

monster_pattern1 = r'(?=(#....##....##....###))'
monster_pattern2 = r'(?=(.#..#..#..#..#..#))'

class Tile:
    def __init__(self, id, img, neighbors) -> None:
        self.id = id
        self.img = img
        self.neighbors = neighbors
    @property
    def left_border(self):
        return ''.join(item[0] for item in self.img)
    @property
    def right_border(self):
        return ''.join(item[-1] for item in self.img)
    @property
    def up_border(self):
        return self.img[0]
    @property
    def down_border(self):
        return self.img[-1]

    @property
    def borders(self):
        return [self.up_border, self.down_border, self.left_border, self.right_border]

    def is_neighbor(self, tile) -> bool:
        if tile.id == self.id:
            return False
        for border in self.borders:
            for border2 in tile.borders:
                if border == border2 or border == border2[::-1]:
                    return True
        return False

    def is_right_neighbor(self, tile) -> bool:
        if tile.id == self.id:
            return False
        if self.right_border == tile.left_border:
            return True

    def update_neighbors(self, all_pics):
        for pic in all_pics:
            tile = Tile(pic[0], pic[1], [])
            if self.is_neighbor(tile):
                self.neighbors.append(tile.id)
    @property
    def neighbors_count(self):
        return len(self.neighbors)

    def _rotate(self):
        tmp_list = []
        row_cnt = len(self.img)
        col_cnt = len(self.img[0])
        for i in range(col_cnt):
            temp_col = []
            for j in range(row_cnt):
                temp_col.append(self.img[j][i])
            tmp_list.append(''.join(temp_col[::-1]))
        return Tile(self.id, tmp_list, self.neighbors)

    def _flip(self):
        return Tile(self.id, self.img[::-1], self.neighbors)

    def all_form(self):
        tiles = []
        tile = self
        for i in range(4):
            tiles.append(tile)
            tile = tile._rotate()
        tile = self._flip()
        for i in range(4):
            tiles.append(tile)
            tile = tile._rotate()
        return tiles

    def show(self):
        print(self.id)
        for row in self.img:
            print(row)
        print(f'neighbors id: {self.neighbors}')


tiles_dict = {}
for pic in all_pics:
    tile = Tile(pic[0], pic[1], [])
    tile.update_neighbors(all_pics)
    tiles_dict[tile.id] = tile

def part1(all_tiles):
    angles_ids = [ tile.id for tile in all_tiles if tile.neighbors_count == 2]
    return reduce(mul, angles_ids, 1)

def get_first_row(tile, tiles_dict, n):
    row = [tile]
    for i in range(n):
        find = False
        tile = row[-1]
        for neighbor_id in tile.neighbors:
            n_tile = tiles_dict[neighbor_id]
            for ntf in n_tile.all_form():
                if tile.right_border == ntf.left_border:
                    row.append(ntf)
                    find = True
                    break
            if find:
                break
    return row

def get_next_row(row, tiles_dict):
    next_row = []
    for tile in row:
        find = False
        for neighbor_id in tile.neighbors:
            n_tile = tiles_dict[neighbor_id]
            for ntf in n_tile.all_form():
                if tile.down_border == ntf.up_border:
                    next_row.append(ntf)
                    find = True
                    break
            if find:
                break
    return next_row

def build_final_piles(first_pile, tiles_dict, n):
    for tile in first_pile.all_form():
        final_piles = []
        row = get_first_row(tile, tiles_dict, n-1)
        if len(row) < n:
            continue
        final_piles.append(row)
        for i in range(n-1):
            next_row = get_next_row(row, tiles_dict)
            if len(next_row) < n:
                break
            final_piles.append(next_row)
            row = next_row
        if len(final_piles) == n:
            return final_piles

def remove_borders(piles):
    whole_pic = []
    for row in piles:
        new_row = []
        for pile in row:
            pile_img = []
            for sub_img in pile.img[1:-1]:
                pile_img.append(sub_img[1:-1])
            new_row.append(pile_img)
        for item in zip(*new_row):
            whole_pic.append(''.join(item))
    return whole_pic

def get_whole_pic(tiles_dict, n):
    angles = [tile for tile  in tiles_dict.values() if tile.neighbors_count == 2]
    first_pile = angles[0]
    final_piles = build_final_piles(first_pile, tiles_dict, n)
    return remove_borders(final_piles)

def get_monster_cnt(image):
    cnt = 0
    for i in range(1, len(image)-1):
        second_finds = set(m.start(0) for m in re.finditer(monster_pattern1, image[i]))
        if len(second_finds) > 0:
            third_finds = set(m.start(0) for m in re.finditer(monster_pattern2, image[i+1]))
            both_math_set = second_finds & third_finds
            if len(both_math_set) > 0:
                for j in both_math_set:
                    if image[i-1][j+18] == '#':
                        cnt += 1
    return cnt

def part2(tiles_dict):
    n = int(math.sqrt(len(tiles_dict)))
    whole_pic = get_whole_pic(tiles_dict, n)
    whole_pic_tile = Tile(0, whole_pic, [])
    all_images = [tile.img for tile in whole_pic_tile.all_form()]
    sea_monsters_img = None
    sea_monsters_cnt = 0
    for image in all_images:
        sea_monsters_cnt = get_monster_cnt(image)
        if sea_monsters_cnt > 0:
            sea_monsters_img = image
            break
    monster_hash_cnt = sum(row.count('#') for row in MONSTER)
    image_hash_cnt = sum(row.count('#') for row in sea_monsters_img)
    return image_hash_cnt - monster_hash_cnt*sea_monsters_cnt

print(part1(tiles_dict.values()))
print(part2(tiles_dict))
