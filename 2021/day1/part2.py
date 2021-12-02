#!/usr/bin/env python3

from typing import List
from part1 import count_increases


def three_measurement(lines: List[str]) -> List[int]:
    lines = [int(line) for line in lines]

    return count_increases([sum(lines[j:j+3]) for j in [i for i in range(len(lines)-2)] if len(lines[j:j+3]) == 3])


if __name__ == '__main__':
    with open("./input.txt", "r") as f:
        print(three_measurement(f.readlines()))
