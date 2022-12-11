import sys
from typing import IO, Generator


DIRMAP: dict[str, tuple[int]] = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}


def move_knot(head: tuple[int], tail: tuple[int]) -> tuple[int]:
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) < 2 and abs(dy) < 2:
        return tail

    xsign = -1 if dx < 0 else 1
    ysign = -1 if dy < 0 else 1

    if dx == 0:
        return (tail[0], tail[1] + (ysign * 1))

    if dy == 0:
        return (tail[0] + (xsign * 1), tail[1])

    return (tail[0] + (xsign * 1), tail[1] + (ysign * 1))


def move_rope(rope: list[tuple[int]], direction: str):
    dirtup = DIRMAP[direction]
    rope[0] = (rope[0][0] + dirtup[0], rope[0][1] + dirtup[1])
    for i in range(1, len(rope)):
        head = rope[i-1]
        tail = rope[i]
        rope[i] = move_knot(head, tail)


def main(knot_count: int, moves: list[str]) -> int:
    rope = [(0, 0) for _ in range(knot_count)]
    tail_locations = set()
    for line in moves:
        direction, distance = line.split()
        distance = int(distance)
        for _ in range(distance):
            move_rope(rope, direction)
            tail_locations.add(rope[-1])
    return len(tail_locations)


if __name__ == "__main__":
    close = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "--stdin":
            infile = sys.stdin
        else:
            infile = open(sys.argv[1], "r")
            close = True
    else:
        infile = open("input.txt", "r")
        close = True

    moves: list[str] = []
    for line in infile.readlines():
        if "\n" in line:
            line = line[:-1]
        moves.append(line)

    print(f"Part 1: {main(2, moves)}")
    print(f"Part 2: {main(10, moves)}")

    if close:
        infile.close()

