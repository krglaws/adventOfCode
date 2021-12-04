#!/usr/bin/env python3
from typing import List


def get_input(path: str) -> List[str]:
    with open(path, "r") as f:
        return [line[:-1] for line in f.readlines()]


def gamma_rate(diagnostic: List[str]) -> str:
    count = len(diagnostic)
    sums = [0 for i in range(len(diagnostic[0]))]

    for i in range(len(sums)): # column
        for j in range(count): # row
            sums[i] += int(diagnostic[j][i])

    return "".join(["0" if n < (count/2) else "1" for n in sums])


def epsilon_rate(gamma: List[str]) -> str:
    return "".join(["1" if bit == "0" else "0" for bit in gamma])


if __name__ == "__main__":
    lines = get_input("./input.txt")
    gamma = gamma_rate(lines)
    epsilon = epsilon_rate(gamma)

    print(int(gamma, 2) * int(epsilon, 2))
