from functools import reduce

def rotate_matrix(m):
	return list(x[::-1] for x in zip(*m))
def flatmap(reverse):
	return [a for b in reverse for a in b]

def transpose(mat):
	return [list(i) for i in zip(*mat)]

def spin_cycle(mat):
	for _ in range(4):
		mat = tilt(mat)
		mat = rotate_matrix(mat)
	return mat
def tilt(mat):
	mat_t = transpose(mat)
	for idx in range(1, len(mat)):
		row = mat[idx]
		row_indexes = list(map(lambda x: x[0], filter(lambda x: x[1] == "O", enumerate(row))))
		for row_idx in row_indexes:
			path = mat_t[row_idx][:idx]
			blockers_on_path = list(map(lambda x: x[0], filter(lambda x: x[1] != ".", enumerate(path))))
			if not blockers_on_path:
				blockers_on_path = [-1]
			target_idx = blockers_on_path[-1] + 1 # because we place it on the next spot
			if target_idx == idx:
				continue
			mat_t[row_idx][target_idx] = "O"
			mat_t[row_idx][idx] = "."
			mat = transpose(mat_t)
	return mat
def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		mat = [list(row) for row in rows]
		mat = tilt(mat)
		max_leverage = len(mat)
	return count_leverage(mat, max_leverage)


def count_leverage(mat, max_leverage):
	total = 0
	for idx, row in enumerate(mat):
		count = len(list(filter(lambda x: x == "O", row)))
		total += (max_leverage - idx) * count
	return total


def string_hash(matrix):
	rows = [','.join(m) for m in matrix]
	return ';'.join(rows)

def pretty_print(matrix):
	for row in matrix:
		print(row)
def part2():
	with open("input.txt") as input_file:
		total_spins = 1000000000
		rows = input_file.read().strip().split('\n')
		mat = [list(row) for row in rows]
		cache = {}
		use_cache = True
		spin = 0
		while spin < total_spins:
			if spin % 10000 == 0:
				print(spin)
			mat = spin_cycle(mat)
			#pretty_print(mat)
			#print(" ")
			if not use_cache:
				spin += 1
				continue
			id = string_hash(mat)
			if id in cache:
				use_cache = False
				period = spin - cache[id]
				remainder = (total_spins - spin) % period
				spin = total_spins - remainder
				#print(period)
				#print(remainder)
				#print(spin)
				#print(" ")
			cache[id] = spin
			spin += 1
	return count_leverage(mat, len(mat))

def count_rocks(mat):
	is_rocks = list(map(lambda x: 1 if x == "O" else 0, flatmap(mat)))
	return reduce(lambda x, y: x + y, is_rocks)


if __name__ == "__main__":
	#print(part1())
	print(part2())
