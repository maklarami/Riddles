from ...commons.commons import import_input
from .aoc_2024_01 import main_list, main_numpy, main_similarity

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

def test_similarity():
    assert main_similarity(list) == 31

real_list = import_input(YEAR="2024", DAY="1")

def test_riddle1():
    result = main_list(real_list)
    print(result)
    assert result == 1651298

def test_riddle2():
    result = main_numpy(real_list)
    print(result)
    assert result == 1651298

def test_riddle3():
    result = main_similarity(real_list)
    print(result)
    assert result == 21306195
