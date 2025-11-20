from ...commons.commons import import_input
from .aoc_2024_04 import part1, part2

DAY = 4
YEAR = 2024

example : str = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def test_example_part1():
    assert part1(example) == 18

def test_example_part2():
    assert part2(example) == 9

def test_input_part1():
    input = import_input(YEAR=YEAR, DAY=DAY)

    assert part1(input) == 2551

def test_input_part2():
    input = import_input(YEAR=YEAR, DAY=DAY)

    assert part2(input) == 1985