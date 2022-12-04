#!/usr/bin/env python3
import sys
from typing import Tuple


def parse_line(line: str) -> Tuple[Tuple[str]]:
    return tuple(
        (int(range_.split('-')[0]), int(range_.split('-')[1])) 
        for range_ in line.split(',')
    )


def contains(pair: Tuple[Tuple[str]]) -> bool:
    elf1, elf2 = pair
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return True
    if elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        return True
    return False


def main(filepath):
    count = 0
    with open(filepath, 'r') as infile:
        while line := infile.readline():
            if contains(parse_line(line)):
                count += 1
    return count


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(sys.argv[1]))
    else:
        print(main("input.txt"))

