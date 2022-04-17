import re
from typing import Tuple, Union
from itertools import combinations

def get_list_data_from_file(file_name, parser=str, sep='\n') -> list:
    file_path = 'data/' + file_name
    sections = open(file_path).read().rstrip().split(sep)
    return [parser(section) for section in sections]

def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))

def convert_str_to_int(number):
    ret = 0
    try:
        ret = int(number)
    except:
        pass
    return ret

def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)

def atoms(text: str, ignore=r'', sep=None) -> Tuple[Union[int, str]]:
    "Parse text into atoms (numbers or strs), possibly ignoring a regex."
    if ignore:
        text = re.sub(ignore, '', text)
    return tuple(map(atom, text.split(sep)))

def atom(text: str) -> Union[float, int, str]:
    "Parse text into a single float or int or str."
    try:
        val = float(text)
        return round(val) if round(val) == val else val
    except ValueError:
        return text

def mapt(fn, *args):
    "Do map(fn, *args) and make the result a tuple."
    return tuple(map(fn, *args))

def dot(A, B):
    "The dot product of two vectors of numbers."
    return sum(a * b for a, b in zip(A, B))

def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return tuple(map(int, re.findall('-?[0-9]+', text)))

def two_sums(nums): return map(sum, combinations(nums, 2))