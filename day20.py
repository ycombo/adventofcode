from functools import reduce
from operator import mul

import utils

def parse_img(img_part: str):
    lines = img_part.splitlines()
    return (utils.ints(lines[0])[0], lines[1:])

images = utils.get_list_data_from_file('day20.txt', parser=parse_img, sep='\n\n')

def borders(img):
    borders = []
    borders.append(img[0])
    borders.append(img[-1])
    borders.append(''.join(item[0] for item in img))
    borders.append(''.join(item[-1] for item in img))
    return borders


def get_neighbor_cnt(img, images):
    cnt = 0
    for border in borders(img[1]):
        for img2 in images:
            if img[0] == img2[0]:
                continue
            for border2 in borders(img2[1]):
                if border == border2 or border == border2[::-1]:
                    cnt += 1
                    break
    return cnt


def part1(images):
    angles = [img[0] for img in images if get_neighbor_cnt(img, images) == 2]
    return reduce(mul, angles, 1)

print(part1(images))