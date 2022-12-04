#!/usr/bin/env python3
import sys

def get_priority(letter: str):
    n = ord(letter[0])
    if n > 96:
        return n - 96
    else:
        return (n - 64) + 26


def get_common(rucksack: str):
    compset = set(rucksack[:len(rucksack)//2])

    for letter in rucksack[len(rucksack)//2:]:
        if letter in compset:
            return letter


def main(filepath: str):
    sum_ = 0
    with open(filepath, 'r') as infile:
        while line := infile.readline():
            sum_ += get_priority(get_common(line))
    return sum_


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(main(sys.argv[1]))
    else:
        print(main("input.txt"))

