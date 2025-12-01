import math
from functools import reduce


def part1():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			winners, candidates = row.split(": ")[1].split(" | ")
			overlap = set(winners.split()).intersection(candidates.split())
			points = int(math.pow(2, len(overlap) - 1)) if overlap else 0
			total += points
	return total


def parse_winners_candidates_tuple(row: str) -> tuple[list[str], ...]:
	return tuple(
		i.split() for i in row.split(": ")[1].strip().split(" | "))


def row_key(row):
	return int(row.split(": ")[0][5::])


def part2():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		original = {
			row_key(row): parse_winners_candidates_tuple(row)
			for row in rows}
		counts = {k: 1 for k in original.keys()}
		for curr in original.keys():
			winners, candidates = original.get(curr)
			overlap = set(winners).intersection(candidates)
			for offsetIndex in range(len(overlap)):
				counts[curr + offsetIndex + 1] += counts[curr]
	return reduce((lambda x, y: x + y), counts.values())


if __name__ == "__main__":
	print(part1())
	print(part2())
