def main(filepath):
    _max = 0
    with open(filepath, 'r') as infile:
        curr = 0
        while line := infile.readline():
            try:
                curr += int(line)
            except:
                _max = max(curr, _max)
                curr = 0
    return _max


if __name__ == '__main__':
    print(main('input.txt'))

