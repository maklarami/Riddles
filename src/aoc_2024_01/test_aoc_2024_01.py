from .aoc_2024_01 import main_list, main_numpy

list : str = """3   4
4   3
2   5
1   3
3   9
3   3"""

def test_main_list():
    assert main_list(list) == 11

def test_main_numpy():
    assert main_numpy(list) == 11