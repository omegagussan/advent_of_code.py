

def part1():
	with open("input.txt") as input_file:
		links = dict()
		rows = input_file.read().strip().split('\n')
		#aaa: you hhh => aaa: [you, hhh] in the links
		for row in rows:
			a, b = row.split(':')
			b_list = [v.strip() for v in b.split(' ') if v.strip() != '']
			links[a.strip()] = b_list
		print(links)

	return count_paths(links, "you", "out")


def count_paths(links: dict[str, list[str]], start: str, end: str, visited=None) -> int:
	if visited is None:
		visited = set()
	if start == end:
		return 1
	visited.add(start)
	total = 0
	for neighbor in links.get(start, []):
		if neighbor not in visited:
			total += count_paths(links, neighbor, end, visited.copy())
	return total

if __name__ == "__main__":
	print(part1())
