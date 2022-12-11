
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


def play_rounds(monkeys: list[Monkey], rounds: int):
    for round_ in range(rounds):
        print(round_)
        for monkey in monkeys:
            for i, item in enumerate(monkey.items):
                operand = item if monkey.inspect_operand == "old" else int(monkey.inspect_operand)
                item = monkey.inspect_operation(item, operand) // 3
                if item % monkey.test_operand == 0:
                    monkeys[monkey.true_action].items.append(item)
                else:
                    monkeys[monkey.false_action].items.append(item)
                monkey.inspections += 1


if __name__ == "__main__":
    lines = []
    with open("input.txt", "r") as infile:
        for line in infile.readlines():
            lines.append(line[:-1] if "\n" in line else line)

    monkeys = parse_monkeys(lines)
    play_rounds(monkeys, 20)
    print(sorted([monkey.inspections for monkey in monkeys]))

