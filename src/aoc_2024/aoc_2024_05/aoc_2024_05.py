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
                    print(f"Violation: {second_page}|{first_page} in {update}")
                    return False
                if first_page in self.is_after[second_page]:
                    print(f"Violation: {first_page}|{second_page} in {update}")
                    return False

        return is_conform

    def reorder(self, update: list[int]) -> list[int]:
        new_update = [update[0]]

        for i in range(1,len(update)):
            page_to_insert = update[i]
            inserted = False
            for j in range (len(new_update)):
                page_to_compare = new_update[j]
                if page_to_insert in self.is_before[page_to_compare]:
                    new_update.insert(j, page_to_insert)
                    inserted = True
                    break

            if not inserted:
                new_update.append(page_to_insert)

        return new_update

def parse_input(input : str) -> tuple[Rules, list[list[int]]]:
    rules = Rules()
    updates_list = []
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

def get_middle(lst: list[int]) -> int:
    return lst[math.floor(len(lst)/2)]

def solve_part_1(input : str) -> int:
    rules, updates_list = parse_input(input)

    sum  = 0
    for update in updates_list:
        if rules.is_conform(update):
            print(f"Hurray: {update}")
            sum += get_middle(update)

    return sum

def solve_part_2(input : str) -> int:
    rules, updates_list = parse_input(input)

    sum  = 0
    for update in updates_list:
        if not rules.is_conform(update):
            print(f"To reorder: {update}")
            reorderd_update = rules.reorder(update)
            print(f"Reordered: {reorderd_update}")
            sum += get_middle(reorderd_update)
    return sum

if __name__ == "__main__":
    print(solve_part_1(""))
    print(solve_part_2(""))