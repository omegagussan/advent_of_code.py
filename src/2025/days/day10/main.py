import pulp
import numpy as np

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

def exact_solver_min_presses(machine):
	num_buttons = len(machine.buttons)
	num_indices = len(machine.joltages)

	# Build the B matrix
	B = np.zeros((num_indices, num_buttons), dtype=int)
	for j, button in enumerate(machine.buttons):
		for idx in button:
			B[idx, j] = 1

	# Define ILP problem
	prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)

	# Variables: x_j >= 0 integer
	x = [pulp.LpVariable(f"x{j}", lowBound=0, cat='Integer') for j in range(num_buttons)]

	# Objective: minimize total presses
	prob += pulp.lpSum(x)

	# Constraints: B @ x == target
	for i in range(num_indices):
		prob += pulp.lpSum(B[i, j] * x[j] for j in range(num_buttons)) == machine.joltages[i]

	# Solve
	prob.solve(pulp.PULP_CBC_CMD(msg=False))

	if prob.status == 1:  # Optimal
		solution = [int(v.value()) for v in x]
		total_presses = sum(solution)
		return total_presses, solution
	else:
		return None, None


def part1():
	with open("input.txt") as input_file:
		machines = parse_machines(input_file)
		total_presses = 0
		for machine in machines:
			print("Solving machine with buttons", machine.buttons)
			presses = bfs_min_presses(machine)
			print(f"Machine completed in {presses} presses")
			total_presses += presses
		print("Total presses:", total_presses)
		return total_presses


def part2():
	with open("input.txt") as input_file:
		machines = parse_machines(input_file)
		total_presses = 0
		for machine in machines:
			print("Solving machine with buttons:", machine.buttons)
			print("and joltages", machine.joltages)
			presses, _ = exact_solver_min_presses(machine)
			print(f"Machine completed in {presses} presses")
			total_presses += presses
		print("Total presses:", total_presses)
		return total_presses


if __name__ == "__main__":
	part1()
	part2()
