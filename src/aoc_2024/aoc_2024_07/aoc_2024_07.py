# Advent of Code 2024 - Day 07 solution
from enum import Enum
from src.utils.commons import permutations_iter


class Operators(Enum):
    ADD = "+"
    MULTIPLY = "*"
    CONCAT = "||"

    def __str__(self):
        return self.value


class Equation:
    def __init__(self, input: str):
        temp_values = input.strip().split(":")
        self.result=int(temp_values[0])
        self.operands=[int(x.strip()) for x in temp_values[1].strip().split(" ")]
        self.num_operators=len(self.operands) - 1

    def __str__(self):
        return f"Equation(result={self.result}, operands={self.operands}, number of operators={self.num_operators})"

    def create_combinations(self, operators : list) -> list[list[Operators]]:
        return permutations_iter(operators, self.num_operators)
        # Aletrnatively: return list(itertools.product(list(Operators), repeat=self.num_operators))

    
    def test_combination(self, combination: list[Operators]) -> bool:
        value = self.operands[0]
        for i in range(len(combination)):
            if combination[i] == Operators.ADD:
                value += self.operands[i+1]
            elif combination[i] == Operators.MULTIPLY:
                value *= self.operands[i+1]
            elif combination[i] == Operators.CONCAT:
                value = int(str(value) + str(self.operands[i+1]))

        if value == self.result:
            return True

def solve_part_1(input : str) -> int:
    total = 0

    for line in input.strip().split("\n"):
        equation = Equation(line)
        combinations = equation.create_combinations([Operators.ADD, Operators.MULTIPLY])
        for combination in combinations:
            if equation.test_combination(list(combination)):
                total += equation.result
                break

    return total

def solve_part_2(input : str) -> int:
    total = 0

    for line in input.strip().split("\n"):
        equation = Equation(line)
        for combination in equation.create_combinations(list(Operators)):
            if equation.test_combination(list(combination)):
                total += equation.result
                break

    return total


        

if __name__ == "__main__":
    pass
