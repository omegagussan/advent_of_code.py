from collections import Counter

def distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

def part1():
    comps = 1000

    # Read points
    with open("input.txt") as f:
        points = [tuple(map(int, line.split(','))) for line in f]

    # Generate all unique edges with distances
    dists = [(distance(points[i], points[j]), i, j)
             for i in range(len(points)) for j in range(i+1, len(points))]
    dists.sort(key=lambda x: x[0])

    # Union-find setup
    parent = list(range(len(points)))
    size = [1]*len(points)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # Process the comps shortest edges
    for _, i, j in dists[:comps]:
        union(i, j)

    # Count component sizes
    comp_sizes = Counter(find(i) for i in range(len(points)))
    largest = sorted(comp_sizes.values(), reverse=True)

    return largest[0]*largest[1]*largest[2]

def part2():
    # Read points
    with open("input.txt") as f:
        points = [tuple(map(int, line.split(','))) for line in f]

    n = len(points)

    # Generate all unique edges with distances
    dists = [(distance(points[i], points[j]), i, j)
             for i in range(n) for j in range(i+1, n)]
    dists.sort(key=lambda x: x[0])

    # Union-find setup
    parent = list(range(n))
    size = [1]*n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True  # merged

    # Process edges until all connected
    for _, i, j in dists:
        if union(i, j):
            if size[find(i)] == n:
                # i and j are the last two junctions to connect the full circuit
                return points[i][0] * points[j][0]

    return -1  # should not reach here

if __name__ == "__main__":
    #print(part1())
    print(part2())
