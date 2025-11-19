from typing import List
import numpy as np

class listpair:
    def __init__(self, input):
        self.first_list : List[int] = []
        self.second_list : List[int] = []

        for line in input.splitlines():
            numbers = line.split("   ")
            self.first_list.append(int(numbers[0]))
            self.second_list.append(int(numbers[1]))

    def __repr__(self) -> str:
        return (
            f"CustomListPairClass (first_list={self.first_list!r}, "
            f"second_list={self.second_list!r})"
        )

    def __str__(self) -> str:
        return (
            f"Custom List Pair Object:\n"
            f"  List 1: {self.first_list}\n"
            f"  List 2: {self.second_list}"
        )

    def sort(self):
        self.first_list.sort()
        self.second_list.sort()

    def distance_np(self) -> int:
        first_array = np.array(self.first_list)
        second_array = np.array(self.second_list)

        distance_array =  first_array - second_array
        return abs(distance_array).sum()

    def distance_list(self) -> int:
        return sum([abs(a - b) for a,b in zip(self.first_list, self.second_list)])

    def similarity(self) -> int:
        result = sum([a*self.second_list.count(a) for a in self.first_list])
        return result

def main_numpy(input: str) -> int:
    lists = listpair(input)
    lists.sort()

    return lists.distance_np()

def main_list(input: str) -> int:
    lists = listpair(input)
    lists.sort()

    return lists.distance_list()

def main_similarity(input: str) -> int:
    lists = listpair(input)
    lists.sort()
    print(lists)
    return lists.similarity()

if __name__ == "__main__":
    list : str = """3   4
4   3
2   5
1   3
3   9
3   3"""
    print(main_list(list))
    print(main_numpy(list))
    print(main_similarity(list))
