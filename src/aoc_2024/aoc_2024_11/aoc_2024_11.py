# Advent of Code 2024 - Day 11 solution

class Tree:
    def __init__(self, input : list[str], max_depth : int):
        self.front = [(0, i) for i in input]
        self.max_depth = max_depth
        self.width = 0
        pass

    def propagate(self) -> bool:

        try:
            level, stone = self.front[-1]
        except IndexError:
            return False

        next_level = level +1

        if next_level < self.max_depth:
            if stone == "0":
                self.front[-1] = ((next_level, "1"))
                return True
            
            length = len(stone)
            if length % 2 == 0:
                middle = length // 2
                self.front[-1] = ((next_level, str(int(stone[:middle]))))
                self.front.append((next_level, str(int(stone[middle:]))))
            else:
                self.front[-1] = ((next_level, str(int(stone)*2024)))
        else:
            if stone == "0":
                self.width += 1  # "0" becomes "1"
            else:
                length = len(stone)
                if length % 2 == 0:
                    self.width += 2  # Splits into 2 stones
                else:
                    self.width += 1  # Multiplied by 2024, stays 1 stone
            self.front.pop()

        return True

def blink(input: list[str]) -> list[str]:
    output = []
    for stone in input:
        if stone == "0":
            output.append("1")
            continue

        length = len(stone)
        if length % 2 == 0:
            middle = length // 2
            output.append(str(int(stone[:middle])))
            output.append(str(int(stone[middle:])))
        else:
            output.append(str(int(stone)*2024))

    return output

def solve_part_1(input : str, blinks : int) -> int:
    stones = [i.strip() for i in input.split(" ")]

    for i in range(blinks):
        stones = blink(stones)
    
    return len(stones)

def solve_part_1a(input : str, blinks : int) -> int:
    stones = [i.strip() for i in input.split(" ")]
    
    tree = Tree(stones, blinks)
    while tree.propagate():
        pass

    return tree.width

def solve_part_2(input: str, blinks: int) -> int:
    stones = {}
    for stone in input.split():
        stones[stone.strip()] = stones.get(stone.strip(), 0) + 1
    
    for _ in range(blinks):
        new_stones = {}
        for stone, count in stones.items():
            if stone == "0":
                new_stones["1"] = new_stones.get("1", 0) + count
            else:
                length = len(stone)
                if length % 2 == 0:
                    left = str(int(stone[:length // 2]))
                    right = str(int(stone[length // 2:]))
                    new_stones[left] = new_stones.get(left, 0) + count
                    new_stones[right] = new_stones.get(right, 0) + count
                else:
                    new_value = str(int(stone) * 2024)
                    new_stones[new_value] = new_stones.get(new_value, 0) + count
        stones = new_stones
    
    print(stones)
    return sum(stones.values())


if __name__ == "__main__":
    solve_part_2("125 17", 75)
