
def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return [line[:-1] for line in f.readlines()]


def find_nums(str_list: list[str]) -> list[int]:
    int_list = []
    for s in str_list:
        left, right = 0, len(s) - 1
        while not s[left].isdigit():
            left += 1
        while not s[right].isdigit():
            right -= 1
        int_list.append(int(s[left] + s[right]))
    return int_list

if __name__ == '__main__':
    input_ = read_input('input.txt')
    nums = find_nums(input_)
    print(sum(nums))

