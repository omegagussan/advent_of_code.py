from itertools import permutations
from functools import reduce

spacer = "^"
replacer = 1000000

def transpose(mat):
	return [list(i) for i in zip(*mat)]

def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		universe = expand(rows)
		universe_t = transpose(universe)
		output_t = expand(universe_t)
		universe = transpose(output_t)
		galaxies = get_galaxies(universe)
		pairs = list(permutations(galaxies, 2))
		dists = [abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]) for p in pairs]
	return reduce((lambda x, y: x + y), dists)// 2


def get_galaxies(universe):
	coordinates = []
	for row_idx, row in enumerate(universe):
		for col_idx, col in enumerate(row):
			if col == "#":
				coordinates.append((row_idx, col_idx))
	return coordinates


def expand(source, replacement="."):
	universe = []
	for row in source:
		r = list(row)
		if not "#" in row:
			universe.append([replacement for _ in r])
			if replacement != ".":
				continue
		universe.append(r)
	return universe



def part2():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		universe = expand(rows, spacer)
		universe_t = transpose(universe)
		output_t = expand(universe_t, spacer)
		universe = transpose(output_t)
		galaxies = get_galaxies(universe)
		total = 0
		pairs = list(permutations(galaxies, 2))
		for p in pairs:
			for x in range(p[0][0], p[1][0]):
				total += replacer if universe[x][p[0][1]] == spacer else 1
			for y in range(p[0][1], p[1][1]):
				total += replacer if universe[p[1][0]][y] == spacer else 1
	
	return total


if __name__ == "__main__":
	print(part1())
	print(part2())
	#93647328 (forgot to change to 10⁶ in replacer
	#857986849428
