import utils

def parse_cups(cups_str):
    return [int(cup) for cup in list(cups_str)]

cups = utils.get_list_data_from_file(
    'day23.txt', parse_cups)[0]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        self.node_location = {}

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.last_node = node
        else:
            self.last_node.next = node
            self.last_node = node

    def insert_nodes(self, position_node, values):
        next_node = position_node.next
        for value in values:
            position_node.next = Node(value)
            self.node_location[value] = position_node.next
            position_node = position_node.next
        position_node.next = next_node
        self.node_location[position_node.value] = position_node

    def create_node_location(self):
        temp_node = self.head
        self.node_location[temp_node.value] = temp_node
        while temp_node.next != self.head:
            temp_node = temp_node.next
            self.node_location[temp_node.value] = temp_node

    def values_list(self):
        temp_node = self.head
        vl = [temp_node.value]
        temp_node = temp_node.next
        while temp_node != self.head:
            vl.append(temp_node.value)
            temp_node = temp_node.next
        return vl


def compute_cups(cups, moves):
    max_cup, min_cup = max(cups), min(cups)
    for i in range(0, moves):
        current_index = i % len(cups)
        current_cup = cups[current_index]
        si, ei = (i+1)%len(cups), (i+4)%len(cups)
        picked_cups = cups[si: ei] if ei > si else cups[si:] + cups[:ei]
        destination_cup = current_cup
        while destination_cup in picked_cups +[current_cup]:
            destination_cup -= 1
            if destination_cup < min_cup:
                destination_cup = max_cup
        dci = cups.index(destination_cup)
        first_part_len = dci + 1
        first_part  = [ cup for cup in cups[:dci+1] if cup not in picked_cups] + picked_cups
        second_part = [ cup for cup in cups[dci+1:] if cup not in picked_cups]
        if dci <= current_index:
            if len(first_part) > first_part_len:
                second_part += first_part[:len(first_part) - first_part_len]
                first_part = first_part[len(first_part) - first_part_len:]
        cups = first_part + second_part
    return cups


def get_picked_cups(current_node):
    picked_cups = []
    for i in range(3):
        picked_cups.append(current_node.next.value)
        current_node.next = current_node.next.next
    return picked_cups


def compute_linked_cups(cll, moves, max_cup, min_cup):
    node = cll.head
    for i in range(0, moves):
        current_cup = node.value
        picked_cups = get_picked_cups(node)
        cll.node_location[node.value] = node
        destination_cup = current_cup
        while destination_cup in picked_cups +[current_cup]:
            destination_cup -= 1
            if destination_cup < min_cup:
                destination_cup = max_cup
        destination_node = cll.node_location[destination_cup]
        cll.insert_nodes(destination_node, picked_cups)
        cll.head = destination_node
        node = node.next
    return cll.values_list()


def build_circular_linked_cups(cups):
    cll = CircularLinkedList()
    for cup in cups:
        cll.add_node(cup)
    cll.last_node.next = cll.head
    cll.create_node_location()
    return cll

def part1(cups, moves):
    cups = compute_cups(cups, moves)
    start_index = cups.index(1)
    return ''.join(str(cup) for cup in cups[start_index+1:] + cups[:start_index])

def part1_linked(cups, moves):
    cll = build_circular_linked_cups(cups)
    cups = compute_linked_cups(cll, moves, 9, 1)
    start_index = cups.index(1)
    return ''.join(str(cup) for cup in cups[start_index+1:] + cups[:start_index])

def part2(cups, moves):
    more_cups = cups + list(range(10, 1000001))
    linked_cups = build_circular_linked_cups(more_cups)
    cups = compute_linked_cups(linked_cups, moves, 1000000, 1)
    start_index = cups.index(1)
    return cups[start_index+1] * cups[start_index+2]

print(part1(cups.copy(), 100))

print(part1_linked(cups.copy(), 100))

print(part2(cups.copy(), 10000000))