from collections import Counter, namedtuple, defaultdict
import itertools
import utils

Food = namedtuple('Food', 'ingredients, allergens')

def parse_food(line):
    ingredients, allergens = line.split(' (contains ')
    return Food(utils.atoms(ingredients), utils.atoms(allergens, ignore=r'[),]'))


foods = utils.get_list_data_from_file(
    'day21.txt', parse_food, sep='\n')


def _get_suspicious_ingredients():
    allergens_in_ingredients = defaultdict(list)
    for food in foods:
        for allergen in food.allergens:
            allergens_in_ingredients[allergen].extend(list(food.ingredients))
    suspicious = defaultdict(set)
    for k, v in allergens_in_ingredients.items():
        _, top_cnt = Counter(v).most_common(1)[0]
        for item, cnt in Counter(v).most_common():
            if cnt == top_cnt:
                suspicious[k].add(item)
            else:
                break
    return suspicious

def part1(suspicious):
    si = set(itertools.chain(*suspicious.values()))
    return sum(utils.quantify(food.ingredients, lambda i: i not in si) for food in foods)


def find_next_ingredient(allergens, ingredients, suspicious, i):
    if i == len(allergens):
        return True
    for ing in suspicious[allergens[i]]:
        if ing not in ingredients:
            ingredients.append(ing)
            if find_next_ingredient(allergens, ingredients, suspicious, i+1):
                return True
            else:
                ingredients.pop()
    return False


def part2(suspicious):
    ingredients = list()
    allergens = sorted(list(suspicious.keys()))
    find_next_ingredient(allergens, ingredients, suspicious, 0)
    return ','.join(ingredients)


suspicious = _get_suspicious_ingredients()
print(part1(suspicious))
print(part2(suspicious))
