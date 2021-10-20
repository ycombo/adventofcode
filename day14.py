import utils
import itertools


def parse_docking_code(line):
    if line.startswith(r'mask'):
        return ('mask', line.split()[-1])
    else:
        return utils.ints(line)


docking_code = utils.get_list_data_from_file(
    'day14.txt', parse_docking_code)


def decode_part1(mask, k, v) -> dict:
    binary = format(v, '036b')
    value = ''.join(a if a != 'X' else b for (a, b) in zip(mask, binary))
    return {k: int(value, 2)}


def decode_part2(mask, k, v) -> dict:
    binary = format(k, '036b')
    value = ''.join(b if a == '0' else a for (a, b) in zip(mask, binary))
    addrs = ['']
    for c in value:
        new_addrs = []
        for addr in addrs:
            if c == 'X':
                new_addrs.append(addr + '1')
                new_addrs.append(addr + '0')
            else:
                new_addrs.append(addr + c)
        addrs = new_addrs

    return {int(addr, 2): v for addr in addrs}


def peter_decode_part2(mask, k, v) -> dict:
    binary = format(k, '036b')
    value = ''.join(a if a == '1' else b if a ==
                    '0' else '{}' for (a, b) in zip(mask, binary))
    ret = {}
    for bits in itertools.product('01', repeat=value.count('{')):
        ret[int(value.format(*bits), 2)] = v
    return ret


def result(decode_method):
    mem_data = dict()
    mask = ''
    for (k, v) in docking_code:
        if k == 'mask':
            mask = v
            continue
        mem_data.update(decode_method(mask, k, v))
    return sum(mem_data.values())


print(result(decode_part1))
print(result(decode_part2))
# print(result(peter_decode_part2))
