def part1():
    comps = 1000
    with open("input.txt") as input_file:
        rows = input_file.read().strip().split('\n')
        points = []
        for row in rows:
            vals = row.strip().split(',')
            x, y, z = [int(v, 10) for v in vals]
            points.append((x, y, z))

        dists = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = distance(points[i], points[j])
                dists.append((d, i, j))   # use indices (not coords) → stable & unique
        dists = sorted(dists, key=lambda x: x[0])

        # connections[i] = which component index point i belongs to
        parent = list(range(len(points)))     # union-find parent pointers
        size = [1] * len(points)              # size of each component

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for d, i, j in dists[:comps]:
            union(i, j)

        comp_sizes = {}
        for i in range(len(points)):
            r = find(i)
            comp_sizes.setdefault(r, 0)
            comp_sizes[r] += 1

        largest = sorted(comp_sizes.values(), reverse=True)

    return largest[0] * largest[1] * largest[2]



def distance(p1, p2):
    return abs(p1[0] - p2[0])* abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) * abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) * abs(p1[2] - p2[2])

if __name__ == "__main__":
    print(part1())
