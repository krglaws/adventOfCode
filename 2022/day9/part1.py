import sys
from typing import IO, Generator


def adjacent(head: tuple[int], tail: tuple[int]) -> bool:
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2


def move(head: tuple[int], tail: tuple[int], distance: int, direction: str) -> Generator[tuple[tuple[int]], None, None]:
    while distance > 0:
        distance -= 1
        if direction == "U":
            head = (head[0], head[1] + 1)
        elif direction == "D":
            head = (head[0], head[1] - 1)
        elif direction == "R":
            head = (head[0] + 1, head[1])
        else:
            head = (head[0] - 1, head[1])

        if not adjacent(head, tail):
            if direction == "U":
                tail = (head[0], head[1] - 1)
            elif direction == "D":
                tail = (head[0], head[1] + 1)
            elif direction == "R":
                tail = (head[0] - 1, head[1])
            else:
                tail = (head[0] + 1, head[1])

        yield head, tail


def main(infile: IO[str]) -> int:
    visited = set()
    head = (0, 0)
    tail = (0, 0)

    visited.add(tail)
    print(tail)

    for line in infile.readlines():
        direction, distance = line[:-1].split()
        distance = int(distance)

        for head, tail in move(head, tail, distance, direction):
            print(tail)
            visited.add(tail)

    return len(visited)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--stdin":
            print(main(sys.stdin))
        else:
            with open(sys.argv[1], "r") as infile:
                print(main(infile))
    else:
        with open("input.txt", "r") as infile:
            print(main(infile))

