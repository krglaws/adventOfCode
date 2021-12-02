#!/usr/bin/env python3

from typing import List, Tuple


def get_input(path: str) -> List[Tuple[str, int]]:
    with open(path, "r") as f:
        lines = f.readlines()
        out = list()
        for line in lines:
            move, dist = line.split(" ")
            out.append((move, int(dist)))
        return out


def get_position(moves: List[Tuple[str, int]]) -> Tuple[int, int]:

    horizontal: int = 0
    vertical: int = 0

    for move in moves:
        m, d = move
        if m == "forward":
            horizontal += d
        elif m == "up":
            vertical -= d
        elif m == "down":
            vertical += d

    return (horizontal, vertical)


if __name__ == "__main__":
    x, y = get_position(get_input("./input.txt"))
    print(x, y)
    print(x*y)
