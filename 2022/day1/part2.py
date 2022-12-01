
def main(filepath):
    elves = []
    with open(filepath, 'r') as infile:
        curr = 0
        while line := infile.readline():
            try:
                curr += int(line)
            except:
                elves.append(curr)
                curr = 0
    return sum(sorted(elves)[-3:])


if __name__ == '__main__':
    print(main('input.txt'))

