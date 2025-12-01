translations = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

backwards_translation = {k[::-1]: v for k, v in translations.items()}


def part1():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			numbers = [c for c in row if c.isnumeric()]
			total += int(numbers[0] + numbers[-1])
	return total


def find_number(lst: list[str], backwards=False):
	remainder = ''
	state = list(reversed(lst)) if backwards else lst.copy()

	while True:
		elem = state.pop(0)
		if elem.isnumeric():
			return elem
		else:
			remainder += elem

		translation = backwards_translation if backwards else translations
		for k, v in translation.items():
			if remainder.endswith(k):
				return str(v)


def part2():
	with open("input.txt") as input_file:
		total = 0
		rows = input_file.read().strip().split('\n')
		for row in rows:
			letter_list = [c for c in row]
			first = find_number(letter_list)
			last = find_number(letter_list, True)
			total += int(first + last)
	return total


if __name__ == "__main__":
	print(part1())
	print(part2())
