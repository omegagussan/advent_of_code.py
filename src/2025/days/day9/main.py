

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

def part2():
	with open("input.txt") as f:
		rows = f.read().strip().split("\n")

	# Parse red corners
	corners = [(int(vals[0]), int(vals[1])) for row in rows if (vals := row.split(","))]

	# Build the perimeter set
	perimeter = set()
	for i in range(len(corners)):
		x1, y1 = corners[i]
		x2, y2 = corners[(i + 1) % len(corners)]
		if x1 == x2:
			for y in range(min(y1, y2), max(y1, y2)+1):
				perimeter.add((x1, y))
		elif y1 == y2:
			for x in range(min(x1, x2), max(x1, x2)+1):
				perimeter.add((x, y1))
		else:
			raise ValueError("Corners must be aligned horizontally or vertically")

	# Function to check rectangle
	def strictly_contains_perimeter(p, q):
		x1, y1 = p
		x2, y2 = q
		minx, maxx = min(x1, x2), max(x1, x2)
		miny, maxy = min(y1, y2), max(y1, y2)
		for px, py in perimeter:
			if minx < px < maxx and miny < py < maxy:
				return True
		return False

	# Iterate over all red-corner pairs
	max_area = 0
	for i in range(len(corners)):
		for j in range(i+1, len(corners)):
			x1, y1 = corners[i]
			x2, y2 = corners[j]
			area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
			if area <= max_area:
				continue
			if strictly_contains_perimeter(corners[i], corners[j]):
				continue
			max_area = area
			print(f"new max area={max_area} from corners {corners[i]} and {corners[j]}")

	return max_area


if __name__ == "__main__":
	#print(part1())
	print(part2())