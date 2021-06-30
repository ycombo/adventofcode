
def get_list_data_from_file(file_name, parser=str, sep='\n') -> list:
    data = []
    file_path = 'data/' + file_name
    sections = open(file_path).read().rstrip().split(sep)
    return [parser(section) for section in sections]




