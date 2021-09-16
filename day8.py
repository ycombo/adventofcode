import utils

instructions = utils.get_list_data_from_file('day8.txt', utils.atoms)


def get_accumulator_value(instructions):
    data_index = 0
    accumulator_value = 0
    operation_index_set = set()
    right_instructions = False
    while data_index not in operation_index_set and data_index < len(instructions):
        operation_index_set.add(data_index)
        opcode, arg = instructions[data_index]
        if opcode == 'jmp':
            data_index += arg
            continue
        elif opcode == 'acc':
            accumulator_value += arg
        data_index += 1
    if data_index == len(instructions):
        right_instructions = True

    return accumulator_value, operation_index_set, right_instructions

accumulator_value, wrong_operation_index_set, _ = get_accumulator_value(instructions)
print(accumulator_value)

def get_right_accumulator_value(operation_index_set, reverse_op=dict(jmp='nop', nop='jmp')):
    for data_index in operation_index_set:
        op, args = instructions[data_index]
        if op not in reverse_op:
            continue
        accumulator_value, _, right_instructions  = \
            get_accumulator_value([*instructions[:data_index], (reverse_op[op] , args), *instructions[data_index+1:]])
        if right_instructions:
            return accumulator_value
    return 0

print(get_right_accumulator_value(wrong_operation_index_set))

        



