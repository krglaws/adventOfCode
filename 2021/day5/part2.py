#!/usr/bin/env python3
from typing import List, Tuple, Dict
from part1 import get_input, make_points


def count_overlaps(path: str):
    total = 0
    point_map: Dict[Tuple[int], int] = {}
    for line in get_input(path):
        p1, p2 = line
        for point in make_points(p1, p2):
            count = point_map.get(point)
            if count == None:
                point_map[point] = 1
            elif count == 1:
                total += 1
                point_map[point] += 1

    return total


if __name__ == "__main__":
    print(count_overlaps("./input.txt"))
