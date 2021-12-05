#!/usr/bin/env python3
from typing import List


class Board():
    
    def __init__(self, board: List[List[int]]):
        self.board = board


def read_input():
    with open("./input.txt") as f:
        lines = readlines()

    draws = [int(num) for num in lines[0][:-1].split(",")]

     
