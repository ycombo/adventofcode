import utils

group_answers = utils.get_list_data_from_file('day6.txt', str.splitlines, sep='\n\n')

def get_every_yes(group_answer):
    answer_set = set(group_answer[0])
    for answer in group_answer[1:]:
        answer_set &= set(answer)
    return answer_set
print(sum(len(set(''.join(group_answer))) for group_answer in group_answers))
print(sum(len(set.intersection(*map(set, group_answer))) for group_answer in group_answers))