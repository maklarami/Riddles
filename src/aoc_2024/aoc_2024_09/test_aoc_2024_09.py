# Tests for Advent of Code 2024 - Day 09
from time import time
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_09.aoc_2024_09 import solve_part_1, solve_part_1_indexing, solve_part_2, solve_part_2_indexing

YEAR = 2024
DAY = 9

# Placeholder for example input data (must be defined in your actual test runner context)
example = "2333133121414131402" 
input = import_input(year=YEAR, day=DAY)

def test_part_1_example():
    # Change 0 to the expected answer
    assert solve_part_1(example) == 1928

def test_part_1_indexing_example():
    # Change 0 to the expected answer
    assert solve_part_1_indexing(example) == 1928

def test_part_2_example():
    # Change 0 to the expected answer
    assert solve_part_2(example) == 2858

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 6367087064415

def test_part_1_indexing_input():
    result = solve_part_1_indexing(input)
    print(f"Part 1 indexing result: {result}")
    assert result == 6367087064415

def test_part_2_input():
    result = solve_part_2(input)
    # Change 0 to the expected answer when ready
    assert result == 6390781891880

def test_part_2_indexing_input():
    result = solve_part_2_indexing(input)
    # Change 0 to the expected answer when ready
    assert result == 6390781891880

def test_performance_part1(benchmark):
    result = benchmark(solve_part_1, input)
    assert result == 6367087064415

def test_performance_part1_indexing(benchmark):
    result = benchmark(solve_part_1_indexing, input)
    assert result == 6367087064415

def test_performance_part2(benchmark):
    result = benchmark(solve_part_2, input)
    assert result == 6390781891880

def test_performance_part2_indexing(benchmark):
    result = benchmark(solve_part_2_indexing, input)
    assert result == 6390781891880