import utils
import math


def split_data(content):
    data = content.split('\n')
    arrive_time = int(data[0])
    bus_ids = [bus_id
               for bus_id in data[1].split(',') if bus_id]

    return (arrive_time, bus_ids)


bus = utils.get_list_data_from_file('day13.txt', split_data, '@')
arrive_time, bus_ids = bus[0]

def part1():
    valid_bus_ids = [int(bus_id) for bus_id in bus_ids if bus_id.isnumeric()]
    return math.prod(min([(bus_id, bus_id - arrive_time % bus_id)
                          for bus_id in valid_bus_ids], key=lambda x: x[1]))


def part2():
    bus_id_with_offset = [(index, int(bus_id)) for index,
                          bus_id in enumerate(bus_ids) if bus_id.isnumeric()]
    step = 1
    start_num = 0
    for (index, bus_id) in bus_id_with_offset:  
            while (start_num + index) % bus_id != 0:
                start_num += step
            step *= bus_id
    return start_num


print(part1())
print(part2())
