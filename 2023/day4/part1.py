def read_input(infile: str) -> list[list[list[str]]]:
    with open(infile, 'r') as f:
        return [[[int(num) for num in half.split()] for half in line[:-1].split(':')[1].split('|')] for line in f.readlines()]


def get_card_value(card: list[list[str]]) -> int:
    n = len(set(card[0]).intersection(set(card[1])))
    return 0 if n == 0 else 2 ** (n - 1)


if __name__ == '__main__':
    cards = read_input('input.txt')
    print(sum(get_card_value(card) for card in cards))

