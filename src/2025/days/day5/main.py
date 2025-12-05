from typing import DefaultDict


def part1():
    tot = 0
    with open("input.txt") as input_file:
        fresh_data, query = input_file.read().strip().split('\n\n')
        fresh_set = set()
        for row in fresh_data.split('\n'):
            a, b = row.split('-')
            a_val = int(a, 10)
            b_val = int(b, 10)
            fresh_set.add((a_val, b_val))
        print(fresh_set)

        for q in query.split('\n'):
            q_val = int(q, 10)
            for a, b in fresh_set:
                if a <= q_val <= b:
                    tot += 1
                    break
    return tot


def part2():
    tot = 0
    with open("input.txt") as input_file:
        fresh_data, query = input_file.read().strip().split('\n\n')
        fresh = list()
        for row in fresh_data.split('\n'):
            a, b = row.split('-')
            a_val = int(a, 10)
            b_val = int(b, 10)
            fresh.append((a_val, b_val))

        # sort by start value
        curr = 0
        fresh_sorted = sorted(fresh, key=lambda x: x[0])
        for a,b in fresh_sorted:
            print(f"a={a}, b={b}, curr={curr}, tot={tot}")
            if curr < a:
                curr = b
                tot += b-a + 1
            elif curr < b:
                tot += b - curr
                curr = b
    return tot
if __name__ == "__main__":
    print(part1())
    print(part2())
