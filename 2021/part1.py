#!/usr/bin/env python3

from typing import List


def count_increases(lines: List[str]) -> int:
    count: int = 0

    for i in range(len(lines)-1):
        l1 = int(lines[i])
        l2 = int(lines[i+1])
        if l2 > l1:
            count += 1

    return count


if __name__ == '__main__':
    with open("./input.txt", "r") as f:
        print(count_increases(f.readlines()))
