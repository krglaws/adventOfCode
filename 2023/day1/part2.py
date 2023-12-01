
def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return [line[:-1] for line in f.readlines()]


def is_digit(s: str, start: int) -> int | None:
    if s[start].isdigit():
        return int(s[start])

    str_to_int = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
    }

    def check_for_dig(s, start, len_):
        dist_from_end = len(s) - start - 1
        if dist_from_end >= len_ - 1:
            sub = s[start:start+len_]
            return str_to_int.get(sub, None)

    for len_ in range(2, 6):
        if (dig := check_for_dig(s, start, len_)) is not None:
            return dig


def find_nums(str_list: list[str]) -> list[int]:
    int_list = []
    for s in str_list:
        left, right = 0, len(s) - 1
        while not (left_dig := is_digit(s, left)):
            left += 1
        while not (right_dig := is_digit(s, right)):
            right -= 1
        int_list.append(left_dig * 10 + right_dig)
    return int_list

if __name__ == '__main__':
    input_ = read_input('input.txt')
    nums = find_nums(input_)
    print(sum(nums))

