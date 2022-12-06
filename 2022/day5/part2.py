

def parse_input(filepath: str) -> tuple[list[list[str]], list[list[int]]]:
    with open(filepath, "r") as infile:
        lines = infile.readlines()

    moves_start = lines.index("\n")
    num_stacks = int(lines[moves_start-1][-3])
    stacks = [[] for _ in range(num_stacks)]

    row = 0
    while lines[row][0] == "[":
        col = 1
        stackno = 0
        while col < len(lines[row]):
            if (c := lines[row][col]).isalpha():
                stacks[stackno].insert(0, c)
            stackno += 1
            col += 4
        row += 1

    moves = []
    for line in lines[moves_start+1:]:
        temp = []
        for w in line.split():
            if w.isdigit():
                temp.append(int(w)-1)
        moves.append(temp)

    return stacks, moves


def do_moves(stacks: list[list[str]], moves: list[list[int]]) -> str:
    for move in moves:
        temp = stacks[move[1]][-(move[0]+1):]
        stacks[move[1]] = stacks[move[1]][:-(move[0]+1)]
        stacks[move[2]] += temp
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    stacks, moves = parse_input("input.txt")
    print(do_moves(stacks, moves))

