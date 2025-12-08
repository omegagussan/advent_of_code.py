from collections import Counter

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
                    next_beam_heads.add(b-1)
                    next_beam_heads.add(b+1)
                    tot += 1
                else:
                    next_beam_heads.add(b)
            print(f"beam_heads={beam_heads}, next_beam_heads={next_beam_heads}, tot={tot}")
            beam_heads = next_beam_heads
            next_beam_heads = set()

    return tot

def part2():
    with open("input.txt") as input_file:
        rows = input_file.read().strip().split('\n')

    # Find S
    start_positions = {j for j, v in enumerate(rows[0]) if v == 'S'}

    # Each starting column begins with 1 beam
    beam = Counter({pos: 1 for pos in start_positions})

    for row in rows:
        new_beam = Counter()

        for pos, count in beam.items():
            tile = row[pos]

            if tile == '^':
                new_beam[pos - 1] += count
                new_beam[pos + 1] += count
            else:
                new_beam[pos] += count

        beam = new_beam

    # Total beams after final row
    return beam.total()


if __name__ == "__main__":
    print(part1())
    print(part2())