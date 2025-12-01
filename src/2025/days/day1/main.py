

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

if __name__ == "__main__":
	print(part1())
