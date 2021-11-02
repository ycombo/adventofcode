import utils
import operator
import itertools
from functools import lru_cache
from collections import Counter

cubes = utils.get_list_data_from_file('day17.txt', list, '\n')


def build_dimention_cubes(init_cubes, dimention):
    return {(x, y, *((0,) * (dimention - 2)))
            for x, row in enumerate(init_cubes) for y, cell in enumerate(row) if cell == '#'}


@lru_cache
def neighbors(cube):
    return {tuple(map(operator.add, cube, delta))
            for delta in set(itertools.product((0, 1, -1), repeat=len(cube))) - {(0,) * len(cube)}}


# def is_cube_active(cube, active_cubes, dimension):
#     neighbor_cubes = neighbors(cube, dimension)
#     active_cnt = sum(1 for nc in neighbor_cubes if nc in active_cubes)
#     return active_cnt == 3 or (active_cnt == 2 and cube in active_cubes)

def neighbors_cnt(active_cubes):
    return Counter(itertools.chain.from_iterable(map(neighbors, active_cubes)))


def run_circles(init_cubes, dimention, times) -> int:
    active_cubes = build_dimention_cubes(init_cubes, dimention)
    for _ in range(times):
        # new_cubes = set()
        # neighbor_cubes = set()
        # for cube in active_cubes:
        #     neighbor_cubes = neighbors.union(neighbors(cube, dimention))
        # for cube in active_cubes.union(neighbor_cubes):
        #     if is_cube_active(cube, active_cubes, dimention):
        #         new_cubes.add(cube)
        # active_cubes = new_cubes
        active_cubes = { cube for cube, cnt in neighbors_cnt(active_cubes).items() if \
            cnt == 3 or (cnt == 2 and cube in active_cubes)}
    return len(active_cubes)


print(run_circles(cubes, 3, 6))
print(run_circles(cubes, 4, 6))
