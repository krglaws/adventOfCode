#!/usr/bin/env python3
import sys
from typing import Generator

MOVES = {
    "X": {
        "A": 3,
        "B": 1,
        "C": 2,
    },
    "Y": {
        "A": 4,
        "B": 5,
        "C": 6,
    }, 
    "Z": {
        "A": 8,
        "B": 9,
        "C": 7,
    },
}


def generate_results(input_path: str) -> Generator[int, None, None]:
    with open(input_path, 'r') as infile:
        while line := infile.readline():
            move, response = line.split()
            yield MOVES[response][move]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sum(generate_results(sys.argv[1])))
    else:
        print(sum(generate_results("./input.txt")))

