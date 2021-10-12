import utils
from collections import Counter
from functools import lru_cache

joltage_ratings = utils.get_list_data_from_file('day10.txt', int)

def joltage_diff_cnt(joltage_ratings):
    joltage_ratings = [0] + joltage_ratings + [max(joltage_ratings) + 3]
    joltage_ratings.sort()
    diff_counter = Counter(joltage_ratings[i+1] - joltage_ratings[i] for i in range(len(joltage_ratings)-1))
    return diff_counter[1] * diff_counter[3]


    # one_diff_cnt, three_diff_cnt = 0, 0
    # start_jolt = 0
    # target_joltage_rating = max(joltage_ratings) + 3
    # joltage_ratings_set.add(target_joltage_rating)
    # while start_jolt != target_joltage_rating:
    #     if (start_jolt + 1) in joltage_ratings_set:
    #         one_diff_cnt += 1
    #         start_jolt += 1
    #         continue
    #     if (start_jolt + 2) in joltage_ratings_set:
    #         start_jolt += 2
    #         continue
    #     if (start_jolt + 3) in joltage_ratings_set:
    #         three_diff_cnt += 1
    #         start_jolt += 3
    #         continue
    # return one_diff_cnt * three_diff_cnt


def combination_cnt(joltage_ratings_set):
    target_joltage_rating = max(joltage_ratings_set)

    @lru_cache
    def find_chain(start_jolt):
        cnt = 0
        for i in range(1, 4):
            if (start_jolt + i) in joltage_ratings_set:
                if start_jolt +i == target_joltage_rating:
                    cnt += 1
                else:
                    cnt += find_chain(start_jolt + i)
        return cnt
    return find_chain(0)

@lru_cache
def peter_cnt(joltage_ratings, prev):
    first, rest = joltage_ratings[0], joltage_ratings[1:]
    if first - prev > 3:
        return 0
    else:
        if not rest:
            return 1
        else:
            return  peter_cnt(rest, prev) + peter_cnt(rest, first)



print(joltage_diff_cnt(joltage_ratings))
print(combination_cnt(set(joltage_ratings)))
print(peter_cnt(tuple(sorted(joltage_ratings)), 0))