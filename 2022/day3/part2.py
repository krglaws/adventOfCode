#!/usr/bin/env python3
import sys
from typing import List


def get_priority(letter: str):
    n = ord(letter[0])
    if n > 96:
        return n - 96
    else:
        return (n - 64) + 26


def get_common(group: List[str]):
    inter = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
    return next(iter(inter))


def main(filepath: str):
    sum_ = 0
    with open(filepath, 'r') as infile:
        group = []
        while line := infile.readline():
            line = line[:-1]
            group.append(line)
            if len(group) == 3:
                common = get_common(group)
                sum_ += get_priority(get_common(group))
                group = []
    return sum_


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(main(sys.argv[1]))
    else:
        print(main("input.txt"))

