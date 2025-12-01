from collections import Counter
from functools import cmp_to_key, reduce

translations = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
non_jokers = list(map(lambda x: str(x), range(2, 10)))
non_jokers.extend(["A", "K", "Q", "T"])


def handle_tie(val: str, joker=False):
	if not joker and val == "J":
		return 0
	return translations.get(val) if translations.get(val) is not None else int(
		val)


def get_type(hand):
	counts = Counter(hand)
	if len(counts) == 1:
		return 6
	if len(counts) == 2:
		if 4 in counts.values():
			return 5
		if 3 in counts.values() and 2 in counts.values():
			return 4
	if len(counts) == 3:
		if 3 in counts.values() and list(counts.values()).count(1) == 2:
			return 3
		if list(counts.values()).count(2) == 2:
			return 2
	if len(counts) == 4:
		return 1
	return 0


cache = {}


def max_by_type(hand: str):
	if cache.get(hand, None):
		return cache[hand]
	joker_hands = find_all_combinations(hand)
	best = max(map(lambda x: get_type(x), joker_hands))
	cache[hand] = best
	return best


def find_all_combinations(hand):
	if not hand:
		return [""]

	current_card = hand[0]
	if current_card == 'J':
		possible_values = "23456789TQKA"
	else:
		possible_values = current_card

	combinations = [
		first_half + second_half
		for first_half in possible_values
		for second_half in find_all_combinations(hand[1:])
	]

	return combinations


def compare(item1, item2):
	compare_hand = get_type(item1) - get_type(item2)
	if compare_hand == 0:
		for i in range(len(item1)):
			compare_card = handle_tie(item1[i]) - handle_tie(
				item2[i])
			if compare_card != 0:
				return compare_card
	return compare_hand


def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		hands = [row[:5] for row in rows]
		hand_to_bid = {row[:5]: int(row[6:]) for row in rows}
		hands = sorted(hands, key=cmp_to_key(compare),
					   reverse=False)
		bid_rank_products = [(rank + 1) * hand_to_bid[hand] for (rank, hand) in
							 enumerate(hands)]
		return reduce((lambda x, y: x + y), bid_rank_products)


def part2():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		hands = [row[:5] for row in rows]
		hand_to_bid = {row[:5]: int(row[6:]) for row in rows}

		hands_with_value = [(hand, max_by_type(hand)) for hand in hands]
		hands_with_value.sort(key=lambda x: (x[1], compare_all(x[0])),
							  reverse=False)
		hands = list(map(lambda x: x[0], hands_with_value))
		bid_rank_products = [(rank + 1) * hand_to_bid[hand] for
							 (rank, hand) in
							 enumerate(hands)]
		return reduce((lambda x, y: x + y), bid_rank_products)


def compare_all(item1):
	return [handle_tie(item1[i]) for i in range(len(item1))]


if __name__ == "__main__":
	print(part1())
	print(part2())
