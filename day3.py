import utils
import math


def get_trees_cnt(data, right_cnt, down_cnt):
    return utils.quantify([row[(i * right_cnt) % len(row)] == '#'
                          for i, row in enumerate(data[::down_cnt])])


def get_multi_trees_product(data, slopes):
    return math.prod([get_trees_cnt(data, slope[0], slope[1]) for slope in slopes])


data = utils.get_list_data_from_file('day3.txt', str)

print(get_trees_cnt(data, 3, 1))
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(get_multi_trees_product(data, slopes))
