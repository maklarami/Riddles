from typing import List
import numpy as np

def main_numpy(input: str) -> int:
    first_list : List[int] = []
    second_list : List[int] = []

    for line in input.splitlines():
        numbers = line.split("   ")
        first_list.append(int(numbers[0]))
        second_list.append(int(numbers[1]))

    first_list.sort()
    second_list.sort()

    first_array = np.array(first_list)
    second_array = np.array(second_list)

    distance_array =  first_array - second_array

    return abs(distance_array).sum()

def main_list(input: str) -> int:
    first_list : List[int] = []
    second_list : List[int] = []

    for line in input.splitlines():
        numbers = line.split("   ")
        first_list.append(int(numbers[0]))
        second_list.append(int(numbers[1]))

    first_list.sort()
    second_list.sort()

    return sum([abs(a - b) for a,b in zip(first_list, second_list)])


if __name__ == "__main__":
    list : str = """3   4
4   3
2   5
1   3
3   9
3   3"""
    print(main_list(list))
    print(main_numpy(list))
