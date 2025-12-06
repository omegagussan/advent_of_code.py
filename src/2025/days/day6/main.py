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

def part2():
    tot = 0
    with open("input.txt") as input_file:
        rows = input_file.read().strip().split('\n')
        #transpose the rows into columns
        cols = []
        for row in rows:
            for i, v in enumerate(row):
                if len(cols) <= i:
                    cols.append([])
                cols[i].append(v)

        val = []
        op = ''
        for col in cols:
            curr = ''.join(col).strip()
            if curr == '':
                tot = update_tot(op, tot, val)
                val = []
                op = ''
            if curr.endswith('+') or curr.endswith('*'):
                val.append(curr[:-1])
                op = curr[-1]
            else:
                val.append(curr)
    tot = update_tot(op, tot, val)
    return tot


def update_tot(op, tot, val):
    val = [v.strip() for v in val if v != '']
    print("here", val, op)
    if op == '+':
        ints = [int(v, 10) for v in val]
        y = sum(ints)
        print(f"adding sum {y}")
        tot += y
    elif op == '*':
        prod = 1
        for v in val:
            prod *= int(v, 10)
        print(f"adding product {prod}")
        tot += prod
    return tot


if __name__ == "__main__":
    #print(part1())
    print(part2())
    #11950004798820