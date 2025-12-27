# Advent of Code 2025 - Day 03 solution

def find_joltage(bank : list[int]) -> int:
    joltage = 0

    first = max(bank[:-1])
    first_index = bank.index(first)

    last = max(bank[first_index+1:])
    joltage = first*10 + last

    return joltage

def find_joltage_2(bank : list[int]) -> int:
    joltage = 0

    index = 0
    for i in range(11,-1,-1):
        if i == 0:
            first = max(bank[index:])
        else:
            first = max(bank[index:-i])

        index = bank.index(first, index)+1
        joltage += first*(10**i)

    return joltage

def solve_part_1(input : str) -> int:
    result = 0
    banks = [[int(i) for i in bank] for bank in input.strip().splitlines()]

    for bank in banks:
        result += find_joltage(bank)

    return result

def solve_part_2(input : str) -> int:
    result = 0
    banks = [[int(i) for i in bank] for bank in input.strip().splitlines()]

    for bank in banks:
        result += find_joltage_2(bank)

    return result

if __name__ == "__main__":
    pass
