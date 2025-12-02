

def part1():
	sum = 0
	with open("input.txt") as input_file:
		pairs = input_file.read().strip().split(',')
		for pair in pairs:
			a, b = pair.split('-')
			start = int(a, 10)
			end = int(b, 10)
			for i in range(start, end + 1):
				if is_repeated_twice(str(i)):
					sum += i
	return sum

def part2():
	sum = 0
	with open("input.txt") as input_file:
		pairs = input_file.read().strip().split(',')
		for pair in pairs:
			a, b = pair.split('-')
			start = int(a, 10)
			end = int(b, 10)
			for i in range(start, end + 1):
				if is_repeated(str(i)):
					sum += i
	return sum

def is_repeated(s: str) -> bool:
	for i in range(2, len(s) + 1):
		if len(s) % i != 0:
			continue
		ps = split_in_equal_parts(s, i)
		found = True
		for p in ps[1:]:
			if p != ps[0]:
				found = False
		if found:
			return True
	return False

def is_repeated_twice(s: str) -> bool:
	first_half = s[:len(s)//2]
	second_half = s[len(s)//2:]
	return first_half == second_half

def split_in_equal_parts(s: str, n: int) -> list[str]:
	part_length = len(s) // n
	return [s[i*part_length:(i+1)*part_length] for i in range(n)]

if __name__ == "__main__":
	print(part1())
	print(part2())
