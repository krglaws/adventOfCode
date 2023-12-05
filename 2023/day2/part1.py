def read_input(infile: str) -> list[list[dict[str, str]]]:
    with open(infile, 'r') as f:
        lines = f.readlines()
    return [[dict(reversed(pick.split()) for pick in round_.split(',')) for round_ in line.split(':')[1].split(';')] for line in lines]


def check_round(maxima: dict[str, str], round_: dict[str, str]):
    for color, quantity in round_.items():
        if maxima[color] < int(quantity):
            return False
    return True


def check_game(maxima: dict[str, str], game: list[dict[str, str]]):
    for round_ in game:
        if not check_round(maxima, round_):
            return False
    print(game)
    return True


def find_possibles(maxima: dict[str, str], games: list[list[dict[str, str]]]):
    return sum(i+1 if check_game(maxima, game) else 0 for i, game in enumerate(games))

if __name__ == '__main__':
    games = read_input('input.txt')
    print(find_possibles({'red': 12, 'green': 13, 'blue': 14}, games))

