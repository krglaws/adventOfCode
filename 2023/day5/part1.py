
DEST = 0
SRC = 1
LEN = 2


def read_input(infile: str):
    with open(infile, 'r') as f:
        seeds = [int(seed) for seed in f.readline().split(':')[1].split()]
        f.readline() # skip one
        map_lines = [line[:-1] for line in f.readlines()]

    maps = []
    curr = []
    for line in map_lines:
        if ':' in line:
            continue
        if not line:
            maps.append(curr)
            curr = []
            continue
        curr.append(tuple(int(x) for x in line.split()))
    if curr:
        maps.append(curr)

    return seeds, maps


def map_to(mapping: list[tuple[int]], x: int) -> int:
        for m in mapping:
            if x >= m[SRC] and x < m[SRC] + m[LEN]:
                return m[DEST] + (x - m[SRC])
        return x


def find_minimum(seeds: list[int], maps: list[tuple[int]]) -> int:
    min_ = float("inf")
    for seed in seeds:
        for mapping in maps:
            seed = map_to(mapping, seed)
        min_ = seed if seed < min_ else min_
    return min_


if __name__ == '__main__':
    seeds, maps = read_input('input.txt')
    print(find_minimum(seeds, maps))

