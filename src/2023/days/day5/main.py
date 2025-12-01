import re

from itertools import groupby


def parse_ints(s: str) -> list[int]:
	return list(map(int, re.findall("\d+", s)))


def split_list(lst):
	return (list(group) for _, group in groupby(lst, lambda x: x != ''))


almanac = [lines.strip() for lines in open("input.txt").readlines()]
seeds = parse_ints(almanac[0])
maps = [[parse_ints(x) for x in m[1:]] for m in split_list(almanac[2:])]


def part1():
	res = []
	for seed in seeds:
		for m in maps:
			for to, start, count in m:
				if start <= seed <= start + count:
					seed += to - start
					break
		res.append(seed)
	return min(res)


def find_overlap(r1, r2):
	r1_start, r1_end = r1
	r2_start, r2_end = r2
	o_start = max(r1_start, r2_start)
	o_end = min(r1_end, r2_end)
	return (o_start, o_end) if o_start <= o_end else None


def shift(r, delta):
	r_start, r_end = r
	return r_start + delta, r_end + delta


def split(r, overlap):
	result = set()

	o_start, o_end = overlap
	r_start, r_end = r

	if r_start < o_start:
		result.add((r_start, o_start - 1))

	if r_end > o_end:
		result.add((o_end + 1, r_end))

	return result


def to_range(start_count):
	start, count = start_count
	return start, start + count - 1


def part2():
	ranges = set(map(to_range, zip(seeds[0::2], seeds[1::2])))

	for m in maps:
		shifted_ranges = set()

		for to, start, count in m:
			for r in ranges.copy():
				result = (start, start + count - 1)
				if overlap := find_overlap(r, result):
					ranges.remove(r)
					ranges |= split(r, overlap)
					shifted_ranges.add(shift(overlap, to - start))
		ranges |= shifted_ranges
	return min(min(ranges))


if __name__ == "__main__":
	print(part1())
	print(part2())
