import re
from collections import defaultdict


def part1():
	with open("input.txt") as input_file:
		parts = input_file.read().strip().split(',')
		return sum([eight_bit_hash(p) for p in parts])


def part2():
	with (open("input.txt") as input_file):
		parts = input_file.read().strip().split(',')
		hashmap = defaultdict(list)
		labelmap = defaultdict(list)
		for p in parts:
			label, _ = re.split('[-=]', p)
			if "-" in p:
				for box in labelmap[label]:
					label_pattern = p.replace("-", "=")
					hashmap[box] = [v for v in hashmap[box] if not v.startswith(label_pattern)]
				labelmap[label] = []
			else:
				hash_label = eight_bit_hash(label)
				if not hashmap[hash_label]:
					hashmap[hash_label].append(p)
					labelmap[label].append(hash_label)
					continue
				else:
					tmp = [p if e.startswith(label + "=") else e for e in hashmap[hash_label]]
					if hashmap[hash_label] == tmp:
						hashmap[hash_label] = list(dict.fromkeys(hashmap[hash_label] + [p]))
						labelmap[label] = list(set(labelmap[label] + [hash_label]))
					else:
						hashmap[hash_label] = tmp
		return get_focusing_power(hashmap)


def matches_label(target, v):
	return target == v.split("=")[0]


def get_focusing_power(hashmap):
	s = 0
	for box, items in hashmap.items():
		for idx, i in enumerate(items):
			v = (int(box) + 1) * (idx + 1) * int(i[-1])
			s += v
	return s


def eight_bit_hash(string: str) -> int:
	val = 0
	for char in string:
		val += ord(char)
		val *= 17
		val = val % 256
	return val


if __name__ == "__main__":
	# print(eight_bit_hash("HASH"))
	print(part1())
	print(part2())
