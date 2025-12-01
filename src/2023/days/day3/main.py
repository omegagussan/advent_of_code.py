from collections import defaultdict

special_characters = set("!@#$%^&*()-+?_=,<>/")
used = 9999999999


def has_adjacent_symbol(schematic: dict, row: int, col: int):
	return any(
		filter(lambda x: x[1] in special_characters,
			   get_adjacent_values(schematic, row, col)))


def get_adjacent_values(schematic: dict, row: int, col: int) -> \
	list[tuple[int, int]]:
	indexes = [(row + 1, col + 1), (row, col + 1), (row - 1, col + 1),
			   (row + 1, col), (row - 1, col), (row, col - 1),
			   (row + 1, col - 1), (row - 1, col - 1)]
	return map(
		lambda x: (x, schematic.get(x) if schematic.get(x) else '.'),
		indexes)


def build_dict(rows):
	return {(row_idx, col_idx): value for row_idx, row in enumerate(rows)
			for (col_idx, value) in enumerate(row)}


def part1():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		schematic = build_dict(rows)
	# add dot at end of each row so remainder don't wrap
	file_content = '.'.join(rows)
	# to compensate for hack above
	row_length = len(rows[0]) + 1
	remainder = ""
	for idx, val in enumerate(file_content):
		if remainder and not val.isnumeric():
			indexes = get_remainder_indexes(idx, remainder, row_length)
			if any(filter(lambda x: has_adjacent_symbol(schematic, x[0], x[1]),
						  indexes)):
				total += int(remainder)
			remainder = ""
		elif val.isnumeric():
			remainder += val
	return total


def get_remainder_indexes(idx, remainder, row_length):
	row = idx // row_length
	col = idx % row_length
	# minus 1 is for we are actually at the char after the last part of the number
	indexes = [(row, col - x - 1) for x in range(len(remainder))]
	return indexes


def part2():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		schematic = build_dict(rows)
	# add dot at end of each row so remainder don't wrap
	file_content = '.'.join(rows)
	# to compensate for hack above
	row_length = len(rows[0]) + 1
	remainder = ""
	gear_candidates = defaultdict(int)
	for idx, val in enumerate(file_content):
		if remainder and not val.isnumeric():
			indexes = get_remainder_indexes(idx, remainder, row_length)
			gears = list(set([i[0] for x in indexes for i in
							  get_adjacent_values(schematic, x[0], x[1]) if i[1] == '*']))
			for gear in gears:
				if gear_candidates[gear] == used:
					continue
				elif gear_candidates[gear] > 0:
					gear_ratio = (int(remainder) * int(gear_candidates[gear]))
					total += gear_ratio
					gear_candidates[gear] = used
				else:
					gear_candidates[gear] += int(remainder)
			remainder = ""
		elif val.isnumeric():
			remainder += val
	return total


if __name__ == "__main__":
	print(part1())
	print(part2())
