

def part1():
	sum = 0
	with open("input.txt") as input_file:
		banks = input_file.read().strip().split('\n')
		for bank in banks:
			maximum = -1
			for i, a in enumerate(bank):
				for b in bank[i+1:]:
					if int(a+b, 10) > maximum:
						maximum = int(a+b, 10)
			sum += maximum
	return sum

if __name__ == "__main__":
	print(part1())
