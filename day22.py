import utils
from collections import deque


def parse_deck(lines):
    return [int(card) for card in lines.split('\n')[1:]]


players_deck = utils.get_list_data_from_file(
    'day22.txt', parse_deck, sep='\n\n')


def compute_player_score(players_deck):
    player_deck = players_deck[0] or players_deck[1]
    return sum(card * (i+1) for i, card in enumerate(reversed(player_deck)))
    return utils.dot(player_deck, range(len(player_deck), 0, -1))


def normal_combat(players_deck):
    players_deck = utils.mapt(deque, players_deck)
    while all(players_deck):
        top_cards = utils.mapt(deque.popleft, players_deck)
        winner = 0 if top_cards[0] > top_cards[1] else 1
        players_deck[winner].extend(sorted(top_cards, reverse=True))
    return players_deck


def part1():
    return compute_player_score(normal_combat(players_deck))


def seen(players_deck, exist_decks):
    players_deck = utils.mapt(tuple, players_deck)
    if players_deck in exist_decks:
        return True
    exist_decks.add(players_deck)
    return False


def recursive_combat(players_deck):
    players_deck = utils.mapt(deque, players_deck)
    exist_decks = set()
    while all(players_deck):
        if seen(players_deck, exist_decks):
            return players_deck[0], []
        top_cards = utils.mapt(deque.popleft, players_deck)
        if all(top_cards[i] <= len(players_deck[i]) for i in (0, 1)):
            sub_decks = recursive_combat(
                [tuple(players_deck[i])[:top_cards[i]] for i in (0, 1)])
            winner = 0 if sub_decks[0] else 1
        else:
            winner = 0 if top_cards[0] > top_cards[1] else 1
        players_deck[winner].extend([top_cards[winner], top_cards[1-winner]])
    return players_deck


def part2():
    return compute_player_score(recursive_combat(players_deck))


print(part1())
print(part2())
