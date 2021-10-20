import utils

direction_order = 'NESWNESW'

oppsite_direction = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

def split_pair(instruction):
    action, values = instruction[0], int(instruction[1:])
    if action == 'L':
        action = 'R'
        values = 360 - values
    return (action, values)

instructions = utils.get_list_data_from_file('day12.txt', split_pair)


def right_rotated_direction(direction, degree):
    return direction_order[direction_order.find(direction) + degree//90]


def transform_directions(action, values, directions_dict):
    if action not in directions_dict:
        action, values = oppsite_direction[action], -values
    directions_dict[action] += values
    return directions_dict


def manhatten_distance(position):
    return sum(abs(v) for _, v in position.items())


def part_1(instructions, position):
    direction = 'E'
    for (action, values) in instructions:
        if action == 'R':
            direction = right_rotated_direction(direction, values)
            continue
        if action == 'F':
            action = direction
        if action in oppsite_direction.keys():
            position = transform_directions(action, values, position)
    return manhatten_distance(position)


def part2(instructions, position):
    waypoints = {
        'N': 1,
        'E': 10
    }
    for (action, values) in instructions:
        if action == 'F':
            for (direction, times) in waypoints.items():
                position = transform_directions(
                    direction, times * values, position)
            continue
        if action == 'R':
            waypoints = {right_rotated_direction(
                k, values): v for (k, v) in waypoints.items()}
            continue
        if action in oppsite_direction.keys():
            waypoints = transform_directions(action, values, waypoints)
    return manhatten_distance(position)


print(part_1(instructions, {'N': 0, 'E': 0}))
print(part2(instructions, {'N': 0, 'E': 0}))
