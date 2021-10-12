import utils
from collections import deque

numbers = utils.get_list_data_from_file('day9.txt', int)

def find_wrong_number(numbers, p=25):
    return utils.first(x for i, x in enumerate(numbers) \
        if i > p and x not in (utils.two_sums(numbers[i-p: i])))

wrong_number = find_wrong_number(numbers)
print(wrong_number)

def find_contiguous_nums(numbers, target):
    sub_seq = deque()
    total = 0
    for x in numbers:
        if total < target:
            sub_seq.append(x)
            total += x
        if total == target and len(sub_seq) >1:
            return sub_seq
        while total > target:
            total -= sub_seq.popleft()
    return [0]
        
contiguous_nums = find_contiguous_nums(numbers, wrong_number)
print (max(contiguous_nums) + min(contiguous_nums))