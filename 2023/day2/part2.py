from part1 import read_input

def mul(*args):
    x = 1
    for num in args:
        x *= num
    return x

def find_minimums(games: list[list[dict[str, str]]]):
    total = 0
    for game in games:
        maxima = {}
        for round_ in game:
            for color, count in round_.items():
                maxima[color] = max(maxima.get(color, 0), int(count))
        total += mul(*maxima.values())
    return total


if __name__ == '__main__':
    games = read_input('input.txt')
    print(find_minimums(games))

