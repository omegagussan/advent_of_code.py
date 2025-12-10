import itertools
from collections import deque
from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Machine:
	state: List[bool]
	buttons: List[Tuple[int, ...]]
	joltages: List[int]

def parse_machines(input_file):
	data = input_file.read().strip().split('\n')
	machines: list[Machine] = []
	for line in data:
		# Indicator light diagram
		d_string = line[line.index('[') + 1:line.index(']')]
		diagram = [c == '#' for c in d_string]

		# Button schematics
		schematics = []
		schematic_part = line[line.index(']') + 1:line.index('{')].strip()
		for s in schematic_part.split(' '):
			if s:
				schematic_tuple = tuple(int(x, 10) for x in s[1: -1].split(','))
				schematics.append(schematic_tuple)

		# Joltage requirements
		joltages = []
		joltage_part = line[line.index('{') + 1:line.index('}')]
		for j in joltage_part.split(','):
			joltages.append(int(j, 10))

		machine = Machine(state=diagram, buttons=schematics, joltages=joltages)
		machines.append(machine)
	return machines

def bfs_min_presses(machine: Machine) -> int:
	start = tuple([False] * len(machine.state))
	target = tuple(machine.state)

	if start == target:
		return 0

	seen = {start}
	queue = deque([(start, 0)])  # (state_tuple, presses)

	while queue:
		state, presses = queue.popleft()
		if state == target:
			return presses

		for button in machine.buttons:
			new_state = list(state)
			for idx in button:
				new_state[idx] = not new_state[idx]
			new_tuple = tuple(new_state)
			if new_tuple not in seen:
				seen.add(new_tuple)
				queue.append((new_tuple, presses + 1))

	raise ValueError("No solution found for machine!")

def part1():
	with open("input.txt") as input_file:
		machines = parse_machines(input_file)
		total_presses = 0
		for machine in machines:
			print("Solving machine with buttons:", machine.buttons)
			presses = bfs_min_presses(machine)
			print(f"Machine completed in {presses} presses")
			total_presses += presses
		print("Total presses:", total_presses)
		return total_presses

if __name__ == "__main__":
	part1()
