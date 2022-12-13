import sys
from typing import Callable

# I cheated on part 2 for this one... Had absolutely no idea how
# to deal with the huge numbers that were being made. Turns out
# the answer is to multiply all the test mod values together to
# produce a magic number, and use THAT as the mod for all monkeys.


class Monkey:

    def __init__(
        self,
        monkey_number: int,
        items: list[int],
        inspect_operation: str,
        inspect_operand: str,
        test_operand: str,
        true_action: int,
        false_action: int
    ):
        self.monkey_number = monkey_number
        self.items = items

        if inspect_operation == "*":
            self.inspect_operation = lambda a, b: a * b
        else:
            self.inspect_operation = lambda a, b: a + b

        self.inspect_operand = inspect_operand
        self.test_operand = test_operand
        self.true_action = true_action
        self.false_action = false_action

        self.inspections = 0


def parse_monkey(lines: list[str]) -> Monkey:
    return Monkey(
        int(lines[0].split()[1][0]),
        [int(item[:-1] if "," in item else item) for item in lines[1].split()[2:]],
        lines[2].split()[4],
        lines[2].split()[5],
        int(lines[3].split()[3]),
        int(lines[4].split()[5]),
        int(lines[5].split()[5]),
    )


def parse_monkeys(lines: list[str]) -> list[Monkey]:
    return [parse_monkey(paragraph.split("\n")) for paragraph in "\n".join(lines).split("\n\n")]


def get_magic_number(monkeys: list[Monkey]) -> int:
    n = 1
    for monkey in monkeys:
        n *= monkey.test_operand
    return n


def play_rounds(monkeys: list[Monkey], worry_op: Callable[[int], int], rounds: int):
    magic_number = get_magic_number(monkeys)
    for round_ in range(rounds):
        #print(round_)
        for monkey in monkeys:
            for item in monkey.items:
                #print(f"Monkey {monkey.monkey_number} inspecting {item}")
                operand = item if monkey.inspect_operand == "old" else int(monkey.inspect_operand)
                item = worry_op(monkey.inspect_operation(item, operand)) % magic_number
                #print(f"new item value = {item}")
                if item % monkey.test_operand == 0:
                    #print(f"{item} tossed to monkey {monkey.true_action}")
                    monkeys[monkey.true_action].items.append(item)
                else:
                    #print(f"{item} tossed to monkey {monkey.false_action}")
                    monkeys[monkey.false_action].items.append(item)
                monkey.inspections += 1
            monkey.items = []


if __name__ == "__main__":
    lines = []
    with open("test.txt", "r") as infile:
        for line in infile.readlines():
            lines.append(line[:-1] if "\n" in line else line)

    monkeys = parse_monkeys(lines)

    if len(sys.argv) > 1 and sys.argv[1] == "--part2":
        play_rounds(monkeys, lambda n: n, 10000)
    else:
        play_rounds(monkeys, lambda n: n // 3, 20)

    second, first = sorted([monkey.inspections for monkey in monkeys])[-2:]

    print(f"Monkey business: {first} * {second} = {second * first}")

