#!/usr/bin/env python3
import sys
from typing import Generator

MOVES = {
    "A": {
        "win": "Y",
        "tie": "X",
    } ,
    "B": {
        "win": "Z",
        "tie": "Y",
    },
    "C": {
        "win": "X",
        "tie": "Z",
    },
}

RESPONSES = {
    "X": 1,
    "Y": 2, 
    "Z": 3,
}


def generate_results(input_path: str) -> Generator[int, None, None]:
    with open(input_path, 'r') as infile:
        while line := infile.readline():
            move, response = line.split()
            score = RESPONSES[response]
            if MOVES[move]["win"] == response:
                score += 6
            elif MOVES[move]["tie"] == response:
                score += 3
            yield score


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sum(generate_results(sys.argv[1])))
    else:
        print(sum(generate_results("./input.txt")))

