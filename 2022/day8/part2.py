import sys
from typing import IO


def get_view(forest: list[list[int]], x: int, y: int, xdir: int, ydir: int) -> int:
    tree_height = forest[y][x]
    view = 0
    x += xdir
    y += ydir
    while 0 <= y < len(forest) and 0 <= x < len(forest[0]):
        if forest[y][x] < tree_height:
            view += 1
        else:
            view += 1
            return view
        x += xdir
        y += ydir
    return view


def get_scenic_score(forest: list[list[int]], x: int, y: int) -> int:
    return get_view(forest, x, y, 1, 0) *\
            get_view(forest, x, y, 0, 1) *\
            get_view(forest, x, y, -1, 0) *\
            get_view(forest, x, y, 0, -1)


def most_scenic_tree(forest: list[list[int]]) -> int:
    highest_score = 0
    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest[0]) - 1):
            highest_score = max(get_scenic_score(forest, x, y), highest_score)
    return highest_score


def read_input(infile: IO[str]) -> list[list[int]]:
    return [[int(height) for height in line[:-1]] for line in infile.readlines()]


if __name__ == "__main__":
    """
    forest = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    print(most_scenic_tree(forest))
    """

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        print(most_scenic_tree(read_input(sys.stdin)))
    else:
        with open("./input.txt", "r") as infile:
            print(most_scenic_tree(read_input(infile)))

