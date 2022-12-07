import sys


def find_start_of_packet(signal: str) -> int:
    left = 0
    last_loc = {}
    for right in range(len(signal)):
        curr = signal[right]
        if curr in last_loc and last_loc[curr] >= left:
            left = last_loc[curr] + 1

        last_loc[curr] = right

        if right - left == 3:
            return right + 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        line = sys.stdin.readline()
    else:
        with open("input.txt") as infile:
            line = infile.readline()

    print(find_start_of_packet(line))

