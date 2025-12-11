import functools

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

def part2():
	with open("input.txt") as input_file:
		links = dict()
		rows = input_file.read().strip().split('\n')
		#aaa: you hhh => aaa: [you, hhh] in the links
		for row in rows:
			a, b = row.split(':')
			b_list = [v.strip() for v in b.split(' ') if v.strip() != '']
			links[a.strip()] = b_list
		print(links)
	#needs to pass via "dac" and "fft" nodes in order
	first = count_paths(links, "svr", "fft")
	print(f"svr -> fft: {first}")
	second = count_paths(links, "fft", "dac")
	print(f"fft -> dac: {second}")
	third = count_paths(links, "dac", "out")
	print(f"dac -> out: {third}")
	return first * second * third


def count_paths(links, start, end):
	@functools.lru_cache(None)
	def dfs(node):
		if node == end:
			return 1
		return sum(dfs(n) for n in links.get(node, []))

	return dfs(start)

if __name__ == "__main__":
	print(part1())
	print(part2())
