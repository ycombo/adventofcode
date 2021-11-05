import utils
import operator

lines = utils.get_list_data_from_file('day18.txt', str, '\n')
OPERATORS = {'+': operator.add, '*': operator.mul}


def reverse_find(line, ops):
    stack = []
    i = len(line) - 1
    while i >= 0:
        if line[i] == ')':
            stack.append(')')
        if line[i] == '(':
            stack.pop()
        if not stack and line[i] in ops:
            break
        i -= 1
    return i


def reverse_find_with_precedence(line):
    index = reverse_find(line, {'*'})
    return index if index > 0 else reverse_find(line, {'+'})


def seperate_line(line, part):
    op_index = reverse_find(line, OPERATORS.keys()) if part == 'part1' else \
        reverse_find_with_precedence(line)
    if op_index <= 0:
        return '', 0, ''
    return line[:op_index], line[op_index], line[op_index + 1:]


def evaluate(line, part):
    line = line.strip()
    if line.isnumeric():
        return int(line)
    left, op, right = seperate_line(line, part)
    if op not in OPERATORS.keys():  # case: (a + b * c)
        return evaluate(line[1:-1], part)
    return OPERATORS[op](evaluate(left, part), evaluate(right, part))


print(sum(evaluate(line, 'part1') for line in lines))
print(sum(evaluate(line, 'part2') for line in lines))
