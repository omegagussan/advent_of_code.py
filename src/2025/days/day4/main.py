

def part1():
	tot = 0
	with open("input.txt") as input_file:
		grid = input_file.read().strip().split('\n')
		print(grid)
		max_i = len(grid)
		max_j = len(grid[0])
		for i in range(max_i):
			for j in range(max_j):
				curr = grid[i][j]
				if curr != '@':
					continue
				adjacent_indices = get_adjacent_indices(i, j, max_i, max_j)
				print(f"At {i},{j} adjacent: {adjacent_indices}")
				adjacent_count = 0
				for ai, aj in adjacent_indices:
					if grid[ai][aj] == '@':
						print(f"  Adjacent {ai},{aj} is {grid[ai][aj]}")
						adjacent_count += 1
				if adjacent_count < 4:
					print(f"Found at {i},{j} with {adjacent_count} adjacent")
					tot += 1
	return tot

# include diagonal adjacency!
def get_adjacent_indices(i: int, j: int, max_i: int, max_j: int) -> list[tuple[int, int]]:
	adj = []
	for di in [-1, 0, 1]:
		for dj in [-1, 0, 1]:
			if di == 0 and dj == 0:
				continue
			ni, nj = i + di, j + dj
			if 0 <= ni < max_i and 0 <= nj < max_j:
				adj.append((ni, nj))
	return adj

def part2():
	tot = 0

	with open("input.txt") as input_file:
		grid = input_file.read().strip().split('\n')

		while True:
			#deep copy
			next_grid = [list(row) for row in grid]

			new_tot = forklift_pass(grid, next_grid, tot)
			grid = next_grid
			if new_tot == tot:
				return tot
			tot = new_tot
			print("Iteration complete, total so far:", tot)


def forklift_pass(grid, next_grid, tot):
	max_i = len(grid)
	max_j = len(grid[0])
	for i in range(max_i):
		for j in range(max_j):
			curr = grid[i][j]
			if curr != '@':
				continue
			adjacent_indices = get_adjacent_indices(i, j, max_i, max_j)
			print(f"At {i},{j} adjacent: {adjacent_indices}")
			adjacent_count = 0
			for ai, aj in adjacent_indices:
				if grid[ai][aj] == '@':
					print(f"  Adjacent {ai},{aj} is {grid[ai][aj]}")
					adjacent_count += 1
			if adjacent_count < 4:
				next_grid[i][j] = '.'
				print(f"Found at {i},{j} with {adjacent_count} adjacent")
				tot += 1
	return tot


if __name__ == "__main__":
	print(part1())
	print(part2())
