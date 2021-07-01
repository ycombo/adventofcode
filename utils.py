
def get_list_data_from_file(file_name, parser=str, sep='\n') -> list:
    data = []
    file_path = 'data/' + file_name
    sections = open(file_path).read().rstrip().split(sep)
    return [parser(section) for section in sections]

def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))
