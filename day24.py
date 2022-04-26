import utils

from collections import defaultdict, namedtuple

Point = namedtuple('Point', 'x, y')


DIRECTIONS = {
    'nw': (-1, 1),
    'ne': (1, 1),
    'e': (2, 0),
    'w': (-2, 0),
    'sw': (-1, -1),
    'se': (1, -1),
}

def parse_tile(line):
    tile = []
    i = 0
    while i < len(line):
        direction = ''
        if line[i] in ('n', 's'):
            direction = line[i:i+2]
            i += 2
        else:
            direction = line[i]
            i += 1
        tile.append(Point(*DIRECTIONS[direction]))
    return tile

tiles = utils.get_list_data_from_file('day24.txt', parse_tile)

def get_flipped_tiles(tiles):
    flipped_tiles = defaultdict(int)
    for tile in tiles:
        sx, sy = 0, 0
        for direction in tile:
            sx += direction.x
            sy += direction.y
        flipped_tiles[(sx, sy)] = (flipped_tiles[(sx, sy)] + 1) % 2
    return flipped_tiles

def part1(flipped_tiles):
    return sum(flipped_tiles.values())


def part2(flipped_tiles):
    for i in range(100):
        black_tiles = { f for f, c in flipped_tiles.items() if c == 1 }
        white_tiles = defaultdict(int)
        for bt in black_tiles:
            black_cnt = 0
            for d in DIRECTIONS.values():
                if (bt[0] + d[0], bt[1] + d[1]) in black_tiles:
                    black_cnt += 1
                else:
                    white_tiles[(bt[0] + d[0], bt[1] + d[1])] += 1
            if black_cnt == 0 or black_cnt > 2:
                flipped_tiles[bt] = 0
        for k, v in white_tiles.items():
            if v == 2:
                flipped_tiles[k] = 1
    return sum(flipped_tiles.values())

flipped_tiles = get_flipped_tiles(tiles)
print(part1(flipped_tiles))
print(part2(flipped_tiles))
