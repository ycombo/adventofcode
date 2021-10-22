import utils

numbers = utils.get_list_data_from_file('day15.txt', int, ',')


# def spoken_number(target_turn):
#     num_turn = {number: index+1 for (index, number) in enumerate(numbers)}
#     current_num, current_turn = 0, len(numbers) + 1
#     for next_turn in range(current_turn + 1, target_turn + 1):
#         next_num = 0
#         if current_num in num_turn:
#             next_num = current_turn - num_turn[current_num]
#         num_turn[current_num] = current_turn
#         current_turn, current_num = next_turn, next_num
#     return current_num

def spoken_number(target_turn):
    num_turn = {number: index for (index, number) in enumerate(numbers[:-1])}
    last_num = numbers[-1]
    for next_turn in range(len(numbers), target_turn):
        new_num = next_turn - 1 - num_turn[last_num] if last_num in num_turn else 0      
        num_turn[last_num] = next_turn - 1
        last_num = new_num
    return last_num


print(spoken_number(2020))
print(spoken_number(30000000))
