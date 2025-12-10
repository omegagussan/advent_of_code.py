import pulp
import numpy as np
from collections import deque
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Machine:
	state: List[bool]
	buttons: List[Tuple[int, ...]]
	joltages: List[int]

def parse_machines(input_file):
	machines = []
	for line in input_file.read().strip().split('\n'):
		diagram = [c == '#' for c in line[line.index('[') + 1:line.index(']')]]
		schematics = [tuple(map(int, s[1:-1].split(','))) for s in line[line.index(']') + 1:line.index('{')].strip().split() if s]
		joltages = list(map(int, line[line.index('{') + 1:line.index('}')].split(',')))
		machines.append(Machine(state=diagram, buttons=schematics, joltages=joltages))
	return machines

def bfs_min_presses(machine: Machine) -> int:
	start, target = tuple([False] * len(machine.state)), tuple(machine.state)
	if start == target:
		return 0

	queue, seen = deque([(start, 0)]), {start}
	while queue:
		state, presses = queue.popleft()
		if state == target:
			return presses
		for button in machine.buttons:
			new_state = tuple(s ^ (i in button) for i, s in enumerate(state))
			if new_state not in seen:
				seen.add(new_state)
				queue.append((new_state, presses + 1))
	raise ValueError("No solution found for machine!")

def exact_solver_min_presses(machine: Machine):
	B = np.zeros((len(machine.joltages), len(machine.buttons)), dtype=int)
	for j, button in enumerate(machine.buttons):
		B[[idx for idx in button], j] = 1

	prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)
	x = [pulp.LpVariable(f"x{j}", lowBound=0, cat='Integer') for j in range(len(machine.buttons))]
	prob += pulp.lpSum(x)
	for i in range(len(machine.joltages)):
		prob += pulp.lpSum(B[i, j] * x[j] for j in range(len(machine.buttons))) == machine.joltages[i]

	prob.solve(pulp.PULP_CBC_CMD(msg=False))
	if prob.status == 1:
		return sum(int(v.value()) for v in x), [int(v.value()) for v in x]
	return None, None

def part1():
	with open("input.txt") as input_file:
		machines = parse_machines(input_file)
		total_presses = sum(bfs_min_presses(machine) for machine in machines)
		print("Total presses:", total_presses)
		return total_presses

def part2():
	with open("input.txt") as input_file:
		machines = parse_machines(input_file)
		total_presses = sum(exact_solver_min_presses(machine)[0] for machine in machines)
		print("Total presses:", total_presses)
		return total_presses

if __name__ == "__main__":
	part1()
	part2()
