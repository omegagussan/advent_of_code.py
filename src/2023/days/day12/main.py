import itertools
import functools

def fill_pounds(s, chars):
	for p in map(iter, itertools.product(chars, repeat=s.count('?'))):
		yield ''.join(c if c != '?' else next(p) for c in s)


def test_valid(string: str, arrangement: list[int]):
	groups = list(filter(lambda x: x, string.split(".")))
	if len(groups) != len(arrangement):
		return False
	for idx, g in enumerate(groups):
		if arrangement[idx] != len(g):
			return False
	return True

def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		total = 0
		for grid, values in [row.split() for row in rows]:
			arrangement = [int(y) for y in values.split(",")]
			g = fill_pounds(grid, "#.")
			valid = list(filter(lambda x: test_valid(x, arrangement), g))
			total += len(valid)

	return total


cache = {}
def part2():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		total = 0
		for grid, values in [row.split() for row in rows]:
			arrangement = 5 * [int(y) for y in values.split(",")]
			unfolded = '?'.join(5 * [grid])
			total += count_matches(unfolded, len(unfolded), tuple(arrangement))
	return total

@functools.cache
def count_matches(pattern, size, arrangement):
	curr, rest = (arrangement[0], arrangement[1:])
	remaining_hashtags = sum(rest) + len(rest)
	
	count = 0
	look_forwards = size - remaining_hashtags - curr + 1
	for start in range(look_forwards):
		if not any(c == "." for c in pattern[start:start+curr]):
			if len(rest) == 0:
				if not any(c == '#' for c in pattern[start+curr:]):
					count += 1
			elif not pattern[start+curr] == '#':
				count += count_matches(
					pattern[start+curr+1:],
				    size-curr-start-1,
				    rest
				)
		if pattern[start] == '#':
			break
	
	return count


if __name__ == "__main__":
	print(part1())
	print(part2())
