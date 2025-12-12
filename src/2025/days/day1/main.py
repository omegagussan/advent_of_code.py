import re


def part1():
	shapes = []
	with open("input.txt") as f:
		*shapes_string, requirements = re.split(r'\r?\n\r?\n', f.read().strip())
		for shape in shapes_string:
			chars = "".join(gift.splitlines()[1:])
			shapes.append(chars.count('#'))

		fits = 0
		for area in requirements.splitlines():
			mx, my, *occurrences = (int(x) for x in re.split(r'[x: ]+', area))
			size = sum(cnt * test for cnt, test in zip(occurrences, shapes))
			if size < mx * my:
				fits += 1

	return fits

if __name__ == "__main__":
	print(part1())
