from part1 import read_input, map_to


def find_minimum(seeds: list[int], maps:list[tuple[int]]) -> int:
    min_ = float('inf')
    for i in range(0, len(seeds), 2):
        print(f'seed range {seeds[i]} + {seeds[i+1]} = {seeds[i] + seeds[i+1]}')
        for seed in range(seeds[i], seeds[i] + seeds[i+1]):
            for mapping in maps:
                seed = map_to(mapping, seed)
            if seed < min_:
                min_ = seed
                print(f"new minimum = {min_}")
    return min_


if __name__ == '__main__':
    seeds, maps = read_input('input.txt')
    print(find_minimum(seeds, maps))
