from re import I
import utils

SUBJECT_KEY = 7

public_keys = utils.get_list_data_from_file('day25.txt', int)


def get_loop_size(target_key):
    val = 1
    i = 0
    while val != target_key:
        i += 1
        val = (val*SUBJECT_KEY) % 20201227
    return i

def get_encryption_key(public_keys):
    card_public_key, door_public_key = public_keys[0], public_keys[1]
    card_loop_size = get_loop_size(card_public_key)
    door_loop_size = get_loop_size(door_public_key)
    encryption_key = 0
    print(door_loop_size, card_public_key)
    for i in range(door_loop_size):
        encryption_key = (i * SUBJECT_KEY) % 20201227
    return encryption_key

public_keys = (5764801, 17807724)
print(get_encryption_key(public_keys))
        