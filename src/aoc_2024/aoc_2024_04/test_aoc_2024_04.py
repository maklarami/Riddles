from ...commons.commons import import_input
from .aoc_2024_04 import main

def test_example():
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

    assert main(example) == 18

def test_input():
    DAY = 4
    YEAR = 2024
    input = import_input(YEAR=YEAR, DAY=DAY)

    assert main(input) == 2551