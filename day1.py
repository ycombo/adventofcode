import utils

def first(iterable, default=None):
    return next(iter(iterable), default)

def two_sum(data_list, target_num):
    items_set = set(data_list)
    return first([x * (target_num - x) for x in items_set if target_num -x in items_set and target_num != 2*x])

def three_sum(data_list, target_num):
    for i, v in enumerate(data_list):
        left_target_num = target_num - v
        product = two_sum(data_list[i+1:], left_target_num)
        if product:
            return v * product
    return 0

    
data = utils.get_list_data_from_file('day1.txt', int)
print(two_sum(data, 2020))
print(three_sum(data, 2020))
