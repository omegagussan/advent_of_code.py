def part1():
    tot = 0
    with open("input.txt") as input_file:
        rows = input_file.read().strip().split('\n')
        cols = []
        for row in rows[:-1]:
            for i, v_string in enumerate([v for v in row.strip().split(' ') if v != '']):
                v = int(v_string, 10)
                if len(cols) <= i:
                    cols.append([])
                print(f"i={i}, v={v}, cols={cols}")
                cols[i].append(v)
        print(cols)
        for i, opt in enumerate([row for row in rows[-1].strip().split(' ') if row != '']):
            if opt.startswith('+'):
                tot += sum(cols[i])
            elif opt.startswith('*'):
                prod = 1
                for c in cols[i]:
                    prod *= c
                tot += prod
    return tot


if __name__ == "__main__":
    print(part1())