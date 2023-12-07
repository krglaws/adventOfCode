from part1 import read_input


def count_cards(cards: list[list[list[str]]]) -> dict[int, int]:
    count_map = { i: 1 for i in range(len(cards)) }
    for i, card in enumerate(cards):
        curr_count = len(set(card[0]).intersection(set(card[1])))
        for j in range(1, curr_count+1):
            if curr_count > len(cards):
                break
            count_map[i + j] += 1 * count_map[i]
    return sum(v for v in count_map.values())


if __name__ == '__main__':
    cards = read_input('input.txt')
    print(count_cards(cards))
