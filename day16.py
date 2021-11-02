import utils
import math
from collections import namedtuple


def parse_rule(rule) -> dict:
    range_set = set()
    rule_parts = rule.split(': ')
    groups = rule_parts[1].split(' or ')
    for group in groups:
        start, end = group.split('-')
        range_set = range_set.union(set(range(int(start), int(end) + 1)))
    return rule_parts[0], range_set


def parse_ticket_sections(fields_str: str, your: str, nearby: str):
    fields = dict(map(parse_rule, fields_str))
    return TicketData(fields=fields,
                      your=utils.ints(your[1]),
                      nearby=[utils.ints(line) for line in nearby[1:]])


# def find_the_only(valid_fields):
#     counter = {}
#     for k, v in valid_fields.items():
#         for index in v:
#             if index not in counter:
#                 counter[index] = [k]
#             else:
#                 counter[index].append(k)
#     for k, v in counter.items():
#         if len(v) == 1:
#             return v[0], k
#     return '', -1


# def get_order(valid_fields):
#     rank = {}
#     while(valid_fields):
#         field, index = find_the_only(valid_fields)
#         del valid_fields[field]
#         rank[field] = index
#     return rank


def part1(ticket_data):
    data_range_set = {d for _, v in ticket_data.fields.items() for d in v}
    return sum(ticket for tickets in ticket_data.nearby for ticket in tickets if ticket not in data_range_set)


def valid_ticket(ticket, data_range_set):
    return all(field in data_range_set for field in ticket)


def elimate_others(possible, index):
    for i in range(len(possible)):
        if i != index:
            possible[i] -= possible[index]


def part2(ticket_data):
    data_range_set = {d for _, v in ticket_data.fields.items() for d in v}
    valid_tickets = [ticket for ticket in ticket_data.nearby if valid_ticket(
        ticket, data_range_set)]
    possible = [set(ticket_data.fields) for _ in range(len(ticket_data.your))]
    while any(len(p) > 1 for p in possible):
        for tickets in valid_tickets:
            for index, ticket in enumerate(tickets):
                for field, range_set in ticket_data.fields.items():
                    if ticket not in range_set:
                        possible[index].discard(field)
                        if len(possible[index]) == 1:
                            elimate_others(possible, index)
    fields = {field: i for i, [field] in enumerate(possible)}
    return math.prod(ticket_data.your[index] for field, index in fields.items() if field.startswith('departure'))


document = utils.get_list_data_from_file('day16.txt', str.splitlines, '\n\n')
TicketData = namedtuple('TicketData', 'fields, your, nearby')
ticket_data = parse_ticket_sections(*document)

print(part1(ticket_data))
print(part2(ticket_data))
