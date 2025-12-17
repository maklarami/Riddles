# Advent of Code 2024 - Day 12 solution

class Region:
    def __init__(self, type : str, position : tuple[int, int]):
        self.type = type
        self.perimeter = 0
        self.area = 0
        self.positions = {position}
        self.unexplored = {position}
        self.fencesNS = set()
        self.fencesEW = set()

    def count_corners(self) -> int:
        corners = 0
        while self.fencesEW or self.fencesNS:
            start_direction = 0
            current = self.fencesEW.pop() 
            direction = 0  # 0: right, 1: up, 2: left, 3: down
            while True:
                continuation = self._find_continuation(current, direction)
                if not continuation:
                    break
                (current, new_direction) = continuation
                if new_direction != direction:
                    corners += 1
                    direction = new_direction
                if direction % 2 == 0:
                    self.fencesEW.remove(current)
                if direction % 2 == 1:
                    self.fencesNS.remove(current)

            if direction != start_direction:
                corners += 1

        self.corners = corners

        return corners
        

    def _find_continuation(self, current, direction) -> tuple[tuple[int, int], int] | None:
        # Define possibilities for each direction: (offset, new_direction, fence_type)
        possibilities = {
        0: [  # moving right
            ((current[0] - 1, current[1] + 1), 1, "NS"),  # turn up
            ((current[0], current[1] + 1), 3, "NS"),      # turn down
            ((current[0], current[1] + 1), 0, "EW"),      # continue right
        ],
        1: [  # moving up
            ((current[0], current[1] - 1), 2, "EW"),      # turn left
            ((current[0], current[1]), 0, "EW"),          # turn right
            ((current[0] - 1, current[1]), 1, "NS"),      # continue up
        ],
        2: [  # moving left
            ((current[0], current[1]), 3, "NS"),          # turn down
            ((current[0] - 1, current[1]), 1, "NS"),      # turn up
            ((current[0], current[1] - 1), 2, "EW"),      # continue left
        ],
        3: [  # moving down
            ((current[0] + 1, current[1]), 0, "EW"),      # turn right
            ((current[0] + 1, current[1] - 1), 2, "EW"),  # turn left
            ((current[0] + 1, current[1]), 3, "NS"),      # continue down
        ],
    }
    
        for possible, new_dir, fence_type in possibilities[direction]:
            fences = self.fencesNS if fence_type == "NS" else self.fencesEW
            if possible in fences:
                return (possible, new_dir)
        
        return None

class Map:
    def __init__(self, input):
        self.map = [[char for char in line.strip()] for line in input.strip().split()]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
    
    def check_neighbour(self, region, row, col, dr, dc, region_type) -> bool:
            new_row = row + dr
            new_col = col + dc
            is_perimeter = False

            if new_row < 0 or new_row >= self.height or new_col < 0 or new_col >= self.width:
                region.perimeter += 1
                is_perimeter = True
            elif not self.visited[new_row][new_col] and self.map[new_row][new_col] == region_type:
                region.unexplored.add((new_row, new_col))
            elif not((new_row, new_col) in region.positions):
                region.perimeter += 1
                is_perimeter = True

            if is_perimeter:
                if dc == -1:
                    region.fencesNS.add((row, col))
                elif dc == 1:
                    region.fencesNS.add((row, new_col))
                elif dr == -1:
                    region.fencesEW.add((row, col))
                elif dr == 1:
                    region.fencesEW.add((new_row, col))
                    

    def explore_region(self, row, col, region_type) -> Region:
        region = Region(region_type, (row, col))

        while region.unexplored:
            (row, col) = region.unexplored.pop()
            self.visited[row][col] = True
            region.positions.add((row,col))
            region.area += 1
            sides = []
            for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                self.check_neighbour(region, row , col, dr, dc, region_type)

        return region

def solve_part_1(input : str) -> int:
    map = Map(input)
    value = 0
    for row in range(map.height):
        for col in range(map.width):
            if not map.visited[row][col]:
                region = map.explore_region(row, col, map.map[row][col])
                value += region.area * region.perimeter
    return value
    

def solve_part_2(input : str) -> int:
    map = Map(input)
    value = 0
    for row in range(map.height):
        for col in range(map.width):
            if not map.visited[row][col]:
                region = map.explore_region(row, col, map.map[row][col])
                corners =region.count_corners()
                value += corners * region.area

                
    return value

if __name__ == "__main__":
    input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
    print(solve_part_2(input))
