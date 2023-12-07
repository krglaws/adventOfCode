from part1 import read_input, inbounds


def sum_gears(schematic: list[str]):
    total = 0
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j] != '*':
                continue
            coords = set()
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0 or not inbounds(schematic, i+k, j+l) or not schematic[i+k][j+l].isdigit():
                        continue
                    front = j+l
                    while front-1 >= 0 and schematic[i+k][front-1].isdigit():
                        front -= 1
                    coords.add((i+k, front))
            if len(coords) > 1:
                mul = 1
                for coord in coords:
                    m = coord[1]
                    s = ""
                    while m < len(schematic[coord[0]]) and schematic[coord[0]][m].isdigit():
                        s += schematic[coord[0]][m]
                        m += 1
                    mul *= int(s)
                total += mul
    return total

if __name__ == '__main__':
    schematic = read_input('input.txt')
    print(sum_gears(schematic))

