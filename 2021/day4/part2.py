#!/usr/bin/env python3
from typing import List
from part1 import read_input, place_token, score


def play(draws: List[int], boards: List[List[List[int]]]):
    for draw in draws:
        i = 0
        while i < len(boards):
            if place_token(draw, boards[i]):
                if len(boards) == 1:
                    return score(boards[i]) * draw
                del boards[i]
            else:
                i += 1


if __name__ == "__main__":
    draws, boards = read_input("./input.txt")
    print(play(draws, boards))
