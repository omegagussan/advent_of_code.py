import math
from functools import reduce


def lcm(arr):
	return reduce(lambda x, y: (x * y) // math.gcd(x, y), arr)


def part1():
	with open("input.txt") as input_file:
		instructions, map_str = input_file.read().strip().split('\n\n')
		mapping = {row[:3]: row.split(' = (')[-1][:-1].split(', ') for row in
				   map_str.split('\n')}

	return solve(instructions, mapping, "AAA", "ZZZ")


def solve(instructions, mapping, start, end):
	curr = start
	counter = 0
	while not curr.endswith(end):
		instruction = instructions[counter % len(instructions)]
		int_instruction = 0 if instruction == "L" else 1
		curr = mapping[curr][int_instruction]
		counter += 1
	return counter


def part2():
	with open("input.txt") as input_file:
		instructions, map_str = input_file.read().strip().split('\n\n')
		print(instructions)
		mapping = {row[:3]: row.split(' = (')[-1][:-1].split(', ') for row in
				   map_str.split('\n')}
		print(mapping)

	curr = [key for key in mapping.keys() if key.endswith('A')]
	periods = [solve(instructions, mapping, c, "Z") for c in curr]
	return lcm(periods)


if __name__ == "__main__":
	print(part1())
	print(part2())
