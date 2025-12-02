

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

def is_repeated_twice(s: str) -> bool:
	first_half = s[:len(s)//2]
	second_half = s[len(s)//2:]
	return first_half == second_half

if __name__ == "__main__":
	print(part1())
