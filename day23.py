import utils

def parse_cups(cups_str):
    return [int(cup) for cup in list(cups_str)]

cups = utils.get_list_data_from_file(
    'day23.txt', parse_cups)[0]

def get_destination_cup(current_cup, max_cup, min_cup):
    destination_cup = current_cup - 1
    return destination_cup if destination_cup >= min_cup else max_cup



def part1(cups):
    max_cup, min_cup = max(cups), min(cups)
    current_index = 0
    for i in range(10):
        current_cup = cups[current_index]
        si, ei = (current_index+1)%len(cups), (current_index+4)%len(cups)
        if ei > si:
            picked_cups = cups[si: ei]
        else:
            picked_cups = cups[si:] + cups[:ei]
        cups = [cup for cup in cups if cup not in picked_cups]
        destination_cup = get_destination_cup(cups[current_index%len(cups)], max_cup, min_cup)
        while destination_cup in picked_cups:
            destination_cup = get_destination_cup(destination_cup, max_cup, min_cup)
        insert_index = cups.index(destination_cup) + 1
        cups = cups[:insert_index] + picked_cups + cups[insert_index:]
        current_index = (cups.index(current_cup) + 1) % len(cups)
    return cups

print(part1(cups))