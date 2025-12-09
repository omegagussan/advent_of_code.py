

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
	with open("input.txt") as input_file:
		rows = input_file.read().strip().split('\n')

	corners = [(int(vals[0]), int(vals[1])) for row in rows if (vals := row.split(','))]

	#create the path between corners in order
	path = set()
	for i in range(len(corners)):
		x1, y1 = corners[i % (len(corners))]
		x2, y2 = corners[(i+1) % (len(corners))]
		if x1 == x2:
			#vertical line
			for y in range(min(y1, y2), max(y1, y2)+1):
				path.add((x1, y))
		elif y1 == y2:
			#horizontal line
			for x in range(min(x1, x2), max(x1, x2)+1):
				path.add((x, y1))
		else:
			raise ValueError("Corners must be aligned either horizontally or vertically")

	#infill the area inside the path
	min_x = min(x for x, y in path)
	max_x = max(x for x, y in path)
	min_y = min(y for x, y in path)
	max_y = max(y for x, y in path)
	for x in range(min_x, max_x+1):
		for y in range(min_y, max_y+1):
			if (x, y) not in path:
				#check if inside path by looking for path points to the left and right
				left = any((xx, y) in path for xx in range(min_x, x))
				right = any((xx, y) in path for xx in range(x+1, max_x+1))
				if left and right:
					path.add((x, y))

	#biggest rectangle area made from two corners
	max_area = 0
	for i in range(len(corners)):
		for j in range(i+1, len(corners)):
			x1, y1 = corners[i]
			x2, y2 = corners[j]
			area = (abs(x2 - x1)+ 1) * (abs(y2 - y1) + 1)
			if area > max_area:
				# check if all points in rectangle are in path
				all_in_path = True
				for x in range(min(x1, x2), max(x1, x2)+1):
					for y in range(min(y1, y2), max(y1, y2)+1):
						if (x, y) not in path:
							all_in_path = False
							break
					if not all_in_path:
						break
				if not all_in_path:
					continue
				max_area = area
				print(f"new max area={max_area} from corners {corners[i]} and {corners[j]}")
	return max_area


if __name__ == "__main__":
	#print(part1())
	print(part2())