def part1():
    with open("input.txt") as input_file:
        rows = input_file.read().strip().split('\n')
        beam_heads = set()
        next_beam_heads = set()
        tot = 0
        for j, v in enumerate(rows[0]):
            if v == 'S':
                beam_heads.add(j)
        print(f"initial beam heads: {beam_heads}")
        for i, row in enumerate(rows):
            for b in beam_heads:
                v = row[b]
                if v == '^':
                    old = len(next_beam_heads)
                    next_beam_heads.add(b-1)
                    next_beam_heads.add(b+1)
                    #if len(next_beam_heads) > old:
                    tot += 1
                else:
                    next_beam_heads.add(b)
            print(f"beam_heads={beam_heads}, next_beam_heads={next_beam_heads}, tot={tot}")
            beam_heads = next_beam_heads
            next_beam_heads = set()

    return tot

if __name__ == "__main__":
    print(part1())