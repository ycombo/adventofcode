import utils


public_keys = utils.get_list_data_from_file('day25.txt', int)


def get_loop_size(target_key):
    val = 1
    i = 0
    while val != target_key:
        i += 1
        val = (val*7) % 20201227
    return i


def get_encryption_key(public_keys):
    card_public_key, door_public_key = public_keys[0], public_keys[1]
    door_loop_size = get_loop_size(door_public_key)
    encryption_key = 1
    for i in range(door_loop_size):
        encryption_key = (encryption_key * card_public_key) % 20201227
    return encryption_key

print(get_encryption_key(public_keys))
