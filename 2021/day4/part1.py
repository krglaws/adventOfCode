#!/usr/bin/env python3
from typing import List, Tuple


def chunk(lines: List[str]):
    for i in range(0, len(lines), 5):
        yield lines[i:i+5]

def read_input(path: str) -> Tuple[List[int], List[List[List[int]]]]:
    with open(path, "r") as f:
        lines = [line[:-1] for line in f.readlines() if line[:-1]]
        draws = [int(num) for num in lines[0].split(",")]
        boards = list(chunk([[int(num) for num in line.split()] for line in lines[1:]]))

    return draws, boards


def check_for_win(board: List[List[int]]) -> bool:
    # check row wins
    for row in board:
        if set(row) == {None}:
            return True

    # check col wins
    for col in range(len(board[0])):
        win = True
        for row in range(len(board)):
            if board[row][col] != None:
                win = False
                break
        if win:
            return True

    return False


def place_token(num: int, board: List[List[int]]):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if num == board[row][col]:
                board[row][col] = None
                if check_for_win(board):
                    return True
                return False
    return False


def score(board: List[List[int]]) -> int:
    return sum([sum(filter(lambda n: n != None, row)) for row in board])


def play(draws: List[int], boards: List[List[List[int]]]):
    for draw in draws:
        for board in boards:
            if place_token(draw, board):
                return score(board) * draw


if __name__ == "__main__":
    draws, boards = read_input("./input.txt")
    print(play(draws, boards))
