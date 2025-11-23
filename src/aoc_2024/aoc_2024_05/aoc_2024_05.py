from collections import defaultdict
import math


class Rules:
    def __init__(self):
        self.is_before = defaultdict(list)
        self.is_after = defaultdict(list)

    def add_rule(self, rule: str):
        first, second = rule.split("|")
        self.is_after[int(first)].append(int(second))
        self.is_before[int(second)].append(int(first))

    def is_conform(self, update : list) -> bool:
        is_conform = True

        for pos1 in range(len(update) - 1):
            first_page = update[pos1]
            for pos2 in range(pos1 + 1, len(update)):
                second_page = update[pos2]
                if second_page in self.is_before[first_page]:
                    print(f"Violation: {second_page}|{update[pos1]} in {update}")
                    return False
                if first_page in self.is_after[second_page]:
                    print(f"Violation: {first_page}|{second_page} in {update}")
                    return False

        return is_conform


def parse_input(input: str) -> tuple[Rules, list[list[int]]]:
    updates_list = []
    rules = Rules()
    is_update = False

    for line in input.splitlines():
        if line.strip() == "":
            is_update = True
        else:
            if is_update:
                    update = list(map(int, line.strip().split(",")))
                    updates_list.append(update)
            else:
                    rules.add_rule(line.strip())

    return rules, updates_list

def solve_part_1(input : str) -> int:
    rules, updates_list = parse_input(input)
    sum  = 0

    for update in updates_list:
        if rules.is_conform(update):
            print(f"Hurray: {update}")
            sum += update[math.floor(len(update)/2)]

    return sum

if __name__ == "__main__":
    print(solve_part_1("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,477"""))