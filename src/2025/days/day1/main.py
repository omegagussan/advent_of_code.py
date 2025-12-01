

def part1():
	with open("input.txt") as input_file:
		zeroes = 0
		curr = 50
		rows = input_file.read().strip().split('\n')
		for row in rows:
			if row[0] == 'L':
				curr -= int(row[1:], 10)
				curr = curr % 100
			else:
				curr += int(row[1:], 10)
				curr = curr % 100
			#print(curr)
			if curr == 0:
				zeroes += 1
	return zeroes

#aka 0x434C49434B
def part2():
	with open("input.txt") as input_file:
		zeroes = 0
		curr = 50
		rows = input_file.read().strip().split('\n')

	for row in rows:
		direction = row[0]
		steps = int(row[1:], 10)

		for _ in range(steps):
			curr = (curr + (1 if direction == 'R' else -1)) % 100
			if curr == 0:
				zeroes += 1

	return zeroes

if __name__ == "__main__":
	print(part1())
	print(part2())
