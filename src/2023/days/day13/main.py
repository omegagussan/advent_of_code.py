def flatmap(reverse):
	return [a for b in reverse for a in b]

def transpose(mat):
	return [list(i) for i in zip(*mat)]

def part1():
	total = 0
	with open("input.txt") as input_file:
		blocks = input_file.read().strip().split('\n\n')
		for rows_str in blocks:
			mat = [list(row) for row in rows_str.split("\n")]
			total += find_fold(mat, True)
			mat_t = transpose(mat)
			total += find_fold(mat_t, False)

	return total


def part2():
	total = 0
	with open("input.txt") as input_file:
		blocks = input_file.read().strip().split('\n\n')
		for rows_str in blocks:
			mat = [list(row) for row in rows_str.split("\n")]
			horizontal = find_fold_tolerate_error(mat, True)
			if horizontal > 0:
				total += horizontal
				continue
			mat_t = transpose(mat)
			total += find_fold_tolerate_error(mat_t, False)

	return total


def find_fold(mat, horizontal=True):
	for i in range(1, len(mat)):
		top = mat[:i]
		bottom = mat[i:]
		assert len(top) + len(bottom) == len(mat)
		overlap = min(i, len(mat) - i)
		reverse = bottom[:overlap][::-1]
		assert len(top[-overlap:]) == len(reverse)
		if top[-overlap:] == reverse:
			return 100 * i if horizontal else i
	return 0


def find_fold_tolerate_error(mat, horizontal=True):
	for i in range(1, len(mat)):
		top = mat[:i]
		bottom = mat[i:]
		assert len(top) + len(bottom) == len(mat)
		overlap = min(i, len(mat) - i)
		reverse = bottom[:overlap][::-1]
		flatmap_reversed = flatmap(reverse)
		errors = [0 if flatmap(top[-overlap:])[i] == flatmap_reversed[i] else 1 for i in range(len(flatmap_reversed))]
		if sum(errors) == 1:
			return 100 * i if horizontal else i
	return 0


if __name__ == "__main__":
	# print(part1())
	print(part2())
# 25233 LOW
# 28167 LOW

#36298 HIGH
#36541 without break