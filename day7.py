from functools import lru_cache
import re
import utils


def parse_bag_rule(line):
    line = re.sub(r' bags?|[.]', '', line)
    outer, inner = line.split(' contain ')
    return outer, dict(map(parse_inner, inner.split(',')))

def parse_inner(text):
    n, color = text.split(maxsplit=1)
    return color, (0 if n == 'no' else int(n))

bag_rules = dict(utils.get_list_data_from_file('day7.txt', parse_bag_rule, sep='\n'))

@lru_cache
def contains(bag, target) -> bool:
    contents = bag_rules.get(bag, {})
    return (target in contents or any(contains(inner, target) for inner in contents))

print(utils.quantify(contains(bag, 'shiny gold') for bag in bag_rules))

def get_bag_cnt(bag)-> int:
    contents = bag_rules.get(bag, {})
    return sum(inner_cnt * (1 + get_bag_cnt(inner)) for inner, inner_cnt in contents.items())

print(get_bag_cnt('shiny gold'))