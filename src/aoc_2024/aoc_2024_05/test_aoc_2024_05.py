from ...commons.commons import import_input
from .aoc_2024_05 import solve_part_1

DAY = 5
YEAR = 2024

def test_part_1_example():
    example = """47|53
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
97,13,75,29,47"""
    assert solve_part_1(example) == 143

def test_part_1_input():
    input = import_input(YEAR=YEAR, DAY=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 3608