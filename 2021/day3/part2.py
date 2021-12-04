#!/usr/bin/env python3
from part1 import get_input
from typing import List


def get_tally(nums: List[str]) -> List[int]:
    count = len(nums)
    sums = [0 for i in range(len(nums[0]))]

    for i in range(len(sums)): # column
        for j in range(count): # row
            sums[i] += int(nums[j][i])

    res = []
    for num in sums:
        if num == (count - num):
            res.append(-1)
        elif num > (count - num):
            res.append(1)
        else:
            res.append(0)

    return res


def bit_filter(lines: List[str], bit: str, pos: int):
    remaining = len(lines)
    i = 0
    while i < remaining and remaining > 1:
        line = lines[i]
        if line[pos] != bit:
            del lines[i]
            remaining -= 1
            continue
        i += 1


def print_arr(arr):
    for num in arr:
        print(num)


if __name__ == "__main__":
    lines = get_input("./input.txt")
    width = len(lines[0])

    oxy_lines = lines
    co2_lines = lines.copy()

    i = 0
    while i < width and len(oxy_lines) > 1:
        print_arr(oxy_lines)
        tally = get_tally(oxy_lines)
        print(f"{tally=}")

        num = tally[i]
        print(f"Filtering by bit {num} at column {i}")
        if num == 1:
            bit_filter(oxy_lines, "1", i)
        elif num == 0:
            bit_filter(oxy_lines, "0", i)
        else:
            bit_filter(oxy_lines, "1", i)
        i += 1

    i = 0
    while i < width and len(co2_lines) > 1:
        print_arr(co2_lines)
        tally = get_tally(co2_lines)
        print(f"{tally=}")

        num = tally[i]
        print(f"Filtering by bit {num} at column {i}")
        if num == 1:
            bit_filter(co2_lines, "0", i)
        elif num == 0:
            bit_filter(co2_lines, "1", i)
        else:
            bit_filter(co2_lines, "0", i)
        i += 1

    oxygen = oxy_lines[0]
    co2 = co2_lines[0]
    print(f"{oxygen=}")
    print(f"{co2=}")
    print(int(oxygen, 2) * int(co2, 2))
