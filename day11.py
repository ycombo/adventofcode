from functools import lru_cache
import utils
from collections import Counter
import itertools
import copy

floor, empty, occupied, boundary = ".L#|"

def one_step_around_item_count(seat_layout, row_index, col_index) -> Counter():
    return Counter(seat_layout[i][j] for i, j in \
        itertools.product([row_index-1, row_index, row_index+1], \
        [col_index-1, col_index, col_index+1]) if i!=row_index or j!=col_index)

def more_step_around_item_count(seat_layout, row_index, col_index) -> Counter():
    @lru_cache
    def get_one_direction_item(row_index, col_index, row_delta, col_delta):
        row_index += row_delta
        col_index += col_delta
        if seat_layout[row_index][col_index] != floor:
            return seat_layout[row_index][col_index]
        else:
            return get_one_direction_item(row_index, col_index, row_delta, col_delta)
                
    items = []
    for i, j in itertools.product([1,0, -1], repeat=2):
        if i==0 and j==0:
            continue
        items.append(get_one_direction_item(row_index, col_index, i, j))
    return Counter(items)

def expand_seat_layout_boundary(seat_layout):
    expand = []
    col_len = len(seat_layout[0])
    expand.append([boundary]* (col_len+2))
    for row in seat_layout:
        expand.append([boundary] + row + [boundary])
    expand.append([boundary]* (col_len+2))
    return expand


def update_seat(expand_layout, item_count_method, action_type, threhold):
    new_layout = copy.deepcopy(expand_layout)
    moved = False
    for i in range(1, len(expand_layout)-1):
        for j in range(1, len(expand_layout[i])-1):
            if expand_layout[i][j] == action_type:
                items_count = item_count_method(expand_layout, i, j)
                if (action_type == occupied and  items_count[occupied] > threhold) or \
                    (action_type == empty and  not items_count[occupied]):
                    new_layout[i][j] = 'L#'.replace(action_type, '')
                    moved = True
                
    return new_layout, moved

    
def get_occupy_seat_cnt(occupy_item_count_method, threhold):
    seat_layout = utils.get_list_data_from_file('day11.txt', list)
    expand_layout = expand_seat_layout_boundary(seat_layout)
    moved = True
    new_layout = expand_layout
    while moved:
        new_layout, moved = update_seat(new_layout, occupy_item_count_method, empty, 0)
        new_layout, moved = update_seat(new_layout, occupy_item_count_method, occupied, threhold)
    seat_cnt = Counter(seat  for row in new_layout for seat in row)
    return seat_cnt['#']

print(get_occupy_seat_cnt(one_step_around_item_count, 3))
print(get_occupy_seat_cnt(more_step_around_item_count, 4))

