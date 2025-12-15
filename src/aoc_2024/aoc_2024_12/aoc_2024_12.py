# Advent of Code 2024 - Day 12 solution

import numpy as np

class Region:
    def __init__(self, type : str, position : tuple[int, int]):
        self.type = type
        self.perimeter = 0
        self.area = 0
        self.positions = {position}
        self.unexplored = {position}  # Set containing the tuple

    def price(self) -> int:
        return self.perimeter * self.area

class Map:
    def __init__(self, input):
        self.map = [[char for char in line.strip()] for line in input.strip().split()]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
    
    def check_neighbour(self, region, row, col, region_type):
            if row < 0 or row >= self.height or col < 0 or col >= self.width:
                region.perimeter += 1
            elif not self.visited[row][col] and self.map[row][col] == region_type:
                region.unexplored.add((row, col))
            elif not((row, col) in region.positions):
                region.perimeter += 1

    def explore_region(self, row, col, region_type) -> Region:
        print(f"New region {region_type} a position {row},{col}")
        region = Region(region_type, (row, col))
        while region.unexplored:
            (row, col) = region.unexplored.pop()
            self.visited[row][col] = True
            region.positions.add((row,col))
            region.area += 1
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                self.check_neighbour(region, row + dr, col + dc, region_type)

        print(f"region size {region.area}, perimeter {region.perimeter}")
        return region.area * region.perimeter
    
    def calculate_value(self) -> int:
        value = 0
        for row in range(self.height):
            for col in range(self.width):
                if not self.visited[row][col]:
                    value += self.explore_region(row, col, self.map[row][col])
        return value

def solve_part_1(input : str) -> int:
    map = Map(input)
    print(map.map)
    print(map.visited)
    value = map.calculate_value()
    
    return value

def solve_part_2(input : str) -> int:
    # Add your Part 2 solution logic here
    return 0

if __name__ == "__main__":
    input = """AAAA
BBCD
BBCC
EEEC"""
    print(solve_part_1(input))
