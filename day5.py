import utils
#import math

# def seat_id(seat_str):
#     row_num = get_num(seat_str[0:7], 'F', 'B', 0, 127)
#     col_num = get_num(seat_str[7:10], 'L', 'R', 0, 7)
#     return row_num*8 +col_num

# def get_num(code, low_letter, high_letter, begin_index, end_index):
#     mid_index = 0
#     for letter in code:
#         mid_index  = (begin_index + end_index) / 2
#         if letter == low_letter:
#            mid_index = math.floor(mid_index)
#            end_index = mid_index
#         if letter == high_letter:
#             mid_index = math.ceil(mid_index)
#             begin_index = mid_index
#     return mid_index

# peter's method
def seat_id(code, table=str.maketrans('FLBR', '0011')):
    return int(code.translate(table), 2)
seat_ids = utils.get_list_data_from_file('day5.txt', seat_id)
print(max(seat_ids))

print(set(range(min(seat_ids), max(seat_ids))) - set(seat_ids))
