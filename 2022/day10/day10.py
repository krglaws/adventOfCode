def print_monitor(monitor: list[str]):
    for line in monitor:
        print("".join(line))
    print("")

def signal_strength(lines: list[str]) -> int:
    monitor = [["." for _ in range(40)] for _ in range(6)]
    sum_ = 0
    cycle = 0
    lineno = 0
    noinc = False
    x = 1
    while lineno < len(lines):
        cycle += 1
        if cycle == 20 or (cycle - 20) % 40 == 0:
            sum_ += cycle * x
        if lines[lineno] == "noop":
            lineno += 1
        else:
            if noinc:
                noinc = False
                x += int(lines[lineno].split()[1])
                lineno += 1
            else:
                noinc = True

        row = cycle // 40
        pixel = cycle - (row * 40)
        if abs(pixel - x) <= 1:
            monitor[row][pixel] = "#"

    print_monitor(monitor)
    return sum_


if __name__ == "__main__":
    with open("input.txt") as infile:
        lines = [line[:-1] for line in infile.readlines()]
    print(signal_strength(lines))
