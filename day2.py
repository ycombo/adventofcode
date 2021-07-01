import utils
import re


def parse_password_policy(line: str):
    "Given '1-3 b: cdefg', return (1, 3, 'b', 'cdefg')."
    a, b, L, pw = re.findall(r'[^-:\s]+', line)
    return (int(a), int(b), L, pw)


def rule_1(policy):
    first_num, second_num, char, pwd = policy
    return first_num <= pwd.count(char) <= second_num


def rule_2(policy):
    first_num, second_num, char, pwd = policy
    pwd_len = len(pwd)
    is_first_exist = first_num <= pwd_len and pwd[first_num-1] == char
    is_second_exist = second_num <= pwd_len and pwd[second_num-1] == char
    return is_first_exist ^ is_second_exist


data = utils.get_list_data_from_file('day2.txt', parse_password_policy)
print(utils.quantify(data, rule_1))
print(utils.quantify(data, rule_2))
