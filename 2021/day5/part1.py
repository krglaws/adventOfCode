#!/usr/bin/env python3
from typing import List, Tuple, Dict


def get_input(path: str) -> List[Tuple[Tuple[int]]]:
    with open(path, "r") as f:
        for line in f.readlines():
            p1, p2 = line[:-1].split(" -> ")
            yield tuple([int(x) for x in p1.split(",")]), tuple([int(x) for x in p2.split(",")])


def make_points(p1: Tuple[int], p2: Tuple[int]):
    startx, starty = p1
    endx, endy = p2
    dx = 1 if startx < endx else -1
    dy = 1 if starty < endy else -1

    while startx != endx or starty != endy:
        yield startx, starty

        if startx != endx:
            startx += dx

        if starty != endy:
            starty += dy

        if startx == endx and starty == endy:
            yield startx, starty


def count_overlaps(path: str):
    total = 0
    point_map: Dict[Tuple[int], int] = {}
    for line in get_input(path):
        p1, p2 = line
        if p1[0] != p2[0] and p1[1] != p2[1]:
            continue
        for point in make_points(p1, p2):
            count = point_map.get(point)
            if count == None:
                point_map[point] = 1
            elif count == 1:
                total += 1
                point_map[point] += count

    return total


if __name__ == "__main__":
    print(count_overlaps("./input.txt"))
