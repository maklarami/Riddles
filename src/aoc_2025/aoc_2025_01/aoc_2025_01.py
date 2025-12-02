# Advent of Code 2025 - Day 01 solution

def solve_part_1(input : str) -> int:
    lines = input.splitlines()
    steps = map(lambda x: (x[0], int(x[1:])), lines)


    counter = 0
    initial = 50
    for step in steps:
        turn, distance = step
        distance = distance % 100
        if turn == 'L':
            if initial >= distance:
                initial -= distance
            else:
                initial = 100 - (distance - initial)
        elif turn == 'R':
            if initial + distance >= 100:
                initial = (initial + distance) - 100
            else:
                initial += distance
        else:
            raise ValueError("Invalid turn direction. Use 'L' or 'R'.")
        if initial == 0:
            counter += 1

    return counter

def solve_part_2_HL(input : str) -> int:
    lines = input.splitlines()
    steps = map(lambda x: (x[0], int(x[1:])), lines)


    counter = 0
    initial = 50
    for step in steps:
        turn, distance = step
        counter += distance // 100
        distance = distance % 100
        if turn == 'L':
            if initial > distance:
                initial -= distance
            else:
                if initial != 0:
                    counter += 1
                initial = 100 - (distance - initial)
            initial %= 100
        elif turn == 'R':
            if initial + distance >= 100:
                if initial != 0:
                    counter += 1
                initial = (initial + distance) - 100
            else:
                initial += distance
            initial %= 100
        else:
            raise ValueError("Invalid turn direction. Use 'L' or 'R'.")
            
    return counter

def solve_part_2(input : str) -> int:
    lines = input.splitlines()
    steps = map(lambda x: (x[0], int(x[1:])), lines)

    counter = 0
    initial = 50
    for step in steps:
        turn, distance = step 
        if turn == 'R':
            result = initial + distance
            counter += result // 100
            initial = result % 100
        if turn == 'L':
            initial = (100 - initial) % 100
            result = initial + distance
            counter += result // 100
            initial = (100 - result % 100)%100
             
    return counter

if __name__ == "__main__":
    pass
