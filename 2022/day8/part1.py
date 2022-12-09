import sys
from typing import IO


def read_input(infile: IO[str]) -> list[list[int]]:
    return [[int(height) for height in line[:-1]] for line in infile.readlines()]


def hike_east_west(forest: list[list[int]], direction: int):
    visible_coords = set()
    if direction == -1:
        inner_range = range(len(forest[0])-1, 0, -1)
    else:
        inner_range = range(0, len(forest[0]), 1)
    for y in range(len(forest)):
        min_height = forest[y][0 if direction == 1 else len(forest[0])-1]
        for x in inner_range:
            if forest[y][x] > min_height or (direction == 1 and x == 0) or (direction == -1 and x == len(forest[0])-1):
                print(f"{(x,y)} is visible")
                visible_coords.add((x, y))
                min_height = forest[y][x]
    return visible_coords


def hike_north_south(forest: list[list[int]], direction: int):
    visible_coords = set()
    if direction == -1:
        inner_range = range(len(forest)-1, 0, -1)
    else:
        inner_range = range(0, len(forest), 1)
    for x in range(len(forest[0])):
        min_height = forest[0 if direction == 1 else len(forest)-1][x]
        for y in inner_range:
            if forest[y][x] > min_height or (direction == 1 and y == 0) or (direction == -1 and y == len(forest)-1):
                print(f"{(x,y)} is visible")
                visible_coords.add((x, y))
                min_height = forest[y][x]
    return visible_coords


def main(forest: list[list[int]]) -> int:
    return len(
        hike_east_west(forest, 1).union(
            hike_east_west(forest, -1).union(
                hike_north_south(forest, 1).union(
                    hike_north_south(forest, -1)
                )
            )
        )
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        forest = read_input(sys.stdin)
    else:
        with open("input.txt") as infile:
            forest = read_input(infile)
    print(main(forest))

