import utils
import re

REQUIRED_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',}
def get_kv_pair(passport) -> dict:
    return dict(re.findall(r'([a-z]+):([^\s]+)', passport))
    
passports = utils.get_list_data_from_file('day4.txt', get_kv_pair, '\n\n')

print(utils.quantify(passports, REQUIRED_KEYS.issubset))

VALIDATORS = {
    'byr': lambda v: 1920 <= utils.convert_str_to_int(v) <= 2002,
    'iyr': lambda v: 2010 <= utils.convert_str_to_int(v) <= 2020,
    'eyr': lambda v: 2020 <= utils.convert_str_to_int(v) <= 2030,
    'hgt': lambda v: 150 <= utils.convert_str_to_int(v.rstrip('cm')) <= 193 or \
                     59 <= utils.convert_str_to_int(v.rstrip('in')) <= 76,
    'hcl': lambda v: re.match('#[0-9a-f]{6}$', v),
    'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda v: re.match('[0-9]{9}$', v)
}

def check_valid(passport):
    return REQUIRED_KEYS.issubset(passport) and \
        all([VALIDATORS[k](passport[k]) for k in REQUIRED_KEYS])

print(utils.quantify(passports, check_valid))
