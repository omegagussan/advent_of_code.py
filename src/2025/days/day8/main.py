def distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

def read_points(filename="input.txt"):
    with open(filename) as f:
        return [tuple(map(int, line.split(','))) for line in f]

def generate_edges(points):
    n = len(points)
    edges = [(distance(points[i], points[j]), i, j)
             for i in range(n) for j in range(i+1, n)]
    edges.sort(key=lambda x: x[0])
    return edges

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def part1(points, comps=1000):
    edges = generate_edges(points)
    uf = UnionFind(len(points))

    for _, i, j in edges[:comps]:
        uf.union(i, j)

    from collections import Counter
    comp_sizes = Counter(uf.find(i) for i in range(len(points)))
    largest = sorted(comp_sizes.values(), reverse=True)
    return largest[0]*largest[1]*largest[2]

def part2(points):
    edges = generate_edges(points)
    n = len(points)
    uf = UnionFind(n)

    for _, i, j in edges:
        if uf.union(i, j):
            if uf.size[uf.find(i)] == n:
                return points[i][0] * points[j][0]

    return -1  # should not happen

if __name__ == "__main__":
    points = read_points("input.txt")
    print("Part 1:", part1(points))
    print("Part 2:", part2(points))
