

def part1():
	tot = 0
	with open("input.txt") as input_file:
		banks = input_file.read().strip().split('\n')
		for bank in banks:
			maximum = -1
			for i, a in enumerate(bank):
				for b in bank[i+1:]:
					if int(a+b, 10) > maximum:
						maximum = int(a+b, 10)
			tot += maximum
	return tot

def part2():
	tot = 0
	with open("input.txt") as input_file:
		banks = input_file.read().strip().split('\n')
		for bank in banks:
			numbers = [int(c, 10) for c in bank]
			number = select_biggest_number(numbers, 12)
			print(number)
			tot += number
	return tot

def select_biggest_number(numbers: list[int], n: int) -> int:
	curr = []
	for i in range(len(numbers)):
		v = numbers[i]
		if not curr:
			curr.append(v)
		else:
			while curr and len(curr) + (len(numbers) - i) > n and curr[-1] < v:
				curr.pop()
			if len(curr) < n:
				curr.append(v)

	return int(''.join(str(c) for c in curr[:n]), 10)

if __name__ == "__main__":
	print(part1())
	print(part2())
