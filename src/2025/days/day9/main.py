

def part1():
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')

	corners = [(int(vals[0]), int(vals[1])) for row in rows if (vals := row.split(','))]
	print(f"corners={corners}")

	#biggest rectangle area made from two corners
	max_area = 0
	for i in range(len(corners)):
		for j in range(i+1, len(corners)):
			x1, y1 = corners[i]
			x2, y2 = corners[j]
			area = (abs(x2 - x1)+ 1) * (abs(y2 - y1) + 1)
			if area > max_area:
				max_area = area
				print(f"new max area={max_area} from corners {corners[i]} and {corners[j]}")
	return max_area

if __name__ == "__main__":
	print(part1())