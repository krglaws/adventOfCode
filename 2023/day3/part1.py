def read_input(infile: str) -> list[str]:
    with open(infile, 'r') as f:
        return [line[:-1] for line in f.readlines()]


def issymbol(schematic: list[str], row: int, col: int) -> bool:
    c = schematic[row][col]
    return not c.isdigit() and c != '.'


def inbounds(schematic, row: int, col: int) -> bool:
    return not (row < 0 or row >= len(schematic) or col < 0 or col >= len(schematic[row]))


def check_num(schematic: list[str], row: int, col: int) -> int:
    i = col + 1
    while i < len(schematic[row]) and schematic[row][i].isdigit():
        i += 1
    num_len = i - col
    for j in range(-1, 2):
        for k in range(-1, num_len + 1):
            if inbounds(schematic, row+j, col+k) and issymbol(schematic, row+j, col+k):
                return True
    return False


def sum_part_numbers(schematic: list[str]) -> int:
    sum_ = 0
    row = 0
    while row < len(schematic):
        col = 0
        in_num = False
        while col < len(schematic[row]):
            if schematic[row][col].isdigit():
                curr_num = ""
                i = col
                while i < len(schematic[row]) and schematic[row][i].isdigit():
                    curr_num += schematic[row][i]
                    i += 1
                if check_num(schematic, row, col):
                    sum_ += int(curr_num)
                col = i
            else:
                col += 1
        row += 1
    return sum_


if __name__ == '__main__':
    schematic = read_input('input.txt')
    print(sum_part_numbers(schematic))

