from functools import reduce


def part1():
	with open("input.txt") as input_file:
		ways_to_race = []
		rows = input_file.read().strip().split('\n')
		times = list(
			map(lambda x: int(x), filter(lambda x: x, rows[0].split(' ')[1::])))
		distances = list(
			map(lambda x: int(x), filter(lambda x: x, rows[1].split(' ')[1::])))
		for race_idx in range(len(times)):
			ways_to_win = 0
			time = times[race_idx]
			for charge in range(1, time):
				run_time = (time - charge)
				run_distance = charge * run_time
				if run_distance > distances[race_idx]:
					ways_to_win += 1
			print(ways_to_win)
			ways_to_race.append(ways_to_win)
	return reduce((lambda x, y: x * y), ways_to_race)


def part2():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')
		time = int(''.join(rows[0].split(' ')[1::]))
		distance = int(''.join(rows[1].split(' ')[1::]))
		ways_to_win = 0
		for charge in range(1, time):
			run_time = (time - charge)
			run_distance = charge * run_time
			if run_distance > distance:
				ways_to_win += 1
	return ways_to_win


if __name__ == "__main__":
	print(part1())
	print(part2())
