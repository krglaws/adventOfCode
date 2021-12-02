#!/usr/bin/env python3

from typing import List, Tuple
from part1 import get_input


def get_position(moves: List[Tuple[str, int]]) -> Tuple[int, int]:

    horizontal: int = 0
    vertical: int = 0
    aim: int = 0

    for move in moves:
        m, d = move
        if m == "forward":
            horizontal += d
            vertical += (aim * d)
        elif m == "up":
            aim -= d
        elif m == "down":
            aim += d

    return (horizontal, vertical)


if __name__ == "__main__":
    x, y = get_position(get_input("./input.txt"))
    print(x, y)
    print(x*y)
