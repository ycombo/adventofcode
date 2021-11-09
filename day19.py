import utils


def parse_message(rules, msg):
    return dict(map(parse_rule, rules)), msg


def parse_rule(rule):
    k, v = tuple(rule.split(':'))
    if "|" in v:
        value = [utils.atoms(
            option.strip(), ignore='["]', sep=' ') for option in v.split('|')]
    else:
        value = utils.atoms(v.strip(), ignore='["]', sep=' ')
    return int(k), value


rules, msg = parse_message(*utils.get_list_data_from_file(
    'day19.txt', str.splitlines, sep='\n\n'))


def check_valid(lines, rule):
    if isinstance(rule, tuple):
        remain_lines = check_valid(lines, rule[0])
        if remain_lines and len(rule) > 1:
            return check_valid(remain_lines, rule[1:])
        else:
            return remain_lines
    if isinstance(rule, list):
        return [line for r in rule for line in check_valid(lines, r)]
    if isinstance(rule, int):
        return check_valid(lines, rules[rule])
    if isinstance(rule, str):
        return [line[1:] for line in lines if line and line[0] == rule]


def part1():
    return utils.quantify('' in check_valid([line], rules[0]) for line in msg)


def part2():
    rules[8] = [(42,), (42, 8)]
    rules[11] = [(42, 31), (42, 11, 31)]
    return utils.quantify('' in check_valid([line], rules[0]) for line in msg)


print(part1())
print(part2())
