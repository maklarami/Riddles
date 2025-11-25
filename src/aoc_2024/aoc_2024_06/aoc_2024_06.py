# Advent of Code 2024 - Day 06 solution

import numpy as np

from src.utils.commons import import_input

class Direction:
    SYMBOL_TO_DIRECTION = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3
}
    DIRECTION_TO_SYMBOL = {v: k for k, v in SYMBOL_TO_DIRECTION.items()}

    SYMBOL_TO_STEP = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)}

    def __init__(self, symbol: str):
        if symbol not in self.SYMBOL_TO_DIRECTION.keys():
            raise ValueError("Invalid direction symbol. Use '^', 'v', '<', or '>'.")
        self.direction = self.SYMBOL_TO_DIRECTION[symbol]

    def step(self) -> tuple[int, int]:
        return self.SYMBOL_TO_STEP[self.direction]

    def __str__(self):
        return self.DIRECTION_TO_SYMBOL[self.direction]
    
    def __int__(self):
        return self.direction
    
    def __repr__(self):
        return self.DIRECTION_TO_SYMBOL[self.direction]
    
    def __eq__(self, other):
        if not isinstance(other, Direction):
            return False
        return self.direction == other.direction
    
    def __hash__(self):
        return hash(self.direction)

class Guard:
    def __init__(self, position: tuple[int, int], direction: str):
        self.position = position
        self.direction = Direction(direction)
        self.positions_history = set()  # Use set for O(1) lookups

    def move(self, new_position: tuple[int, int] = None):
        self.position = (self.position[0] + new_position[0], self.position[1] + new_position[1])
    
    def turn_right(self):
        new_direction = (int(self.direction) + 1) % 4
        symbol = self.direction.DIRECTION_TO_SYMBOL[new_direction]
        self.direction = Direction(symbol)
    
    def save_current_position(self):
        self.positions_history.add((self.position, self.direction))

    def is_in_known_position(self) -> bool:
        return (self.position, self.direction) in self.positions_history

class Board:
    def __init__(self, input: str):
        grid = []
        self.guard = None

        for line in input.splitlines():
            row = []
            for char in line.strip():
                if char in ['.']:
                    row.append(True)
                elif char == '#':
                    row.append(False)
                elif char in ['^', 'v', '<', '>']:
                    self.guard = Guard(position=(len(grid), len(row)), direction=char)
                    row.append(True)
                else:
                    raise ValueError(f"Invalid character in input: {char}")
            grid.append(row)

        self.grid = np.array(grid)
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.visited_grid = np.zeros((self.width, self.height))
        self.set_as_visited(self.guard.position)    

    def add_obstacle(self, position: tuple[int, int]):
        self.grid[position] = False

    def remove_obstacle(self, position: tuple[int, int]):
        self.grid[position] = True

    def set_as_visited(self, position: tuple[int, int]):
        self.visited_grid[position] = 1

    def move_guard(self) -> bool:
        step = self.guard.direction.step()
        current_row, current_col = self.guard.position

        new_position = (current_row + step[0], current_col + step[1])

        if not self.check_within_bounds(new_position):
            return False
        if not self.check_if_free_field(new_position):
            self.guard.turn_right()
            return True
        
        self.guard.move(step)
        self.set_as_visited(self.guard.position)
        
        return True

    def check_if_free_field(self, position: tuple[int, int]) -> bool:
        return self.grid[position]
    
    def check_within_bounds(self, position: tuple[int, int]) -> bool:
        row, col = position
        return 0 <= row < self.height and 0 <= col < self.width
    
    def __str__(self):
        display = ""
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) == self.guard.position:
                    display += str(self.guard.direction)
                elif not self.grid[r, c]:
                    display += "#"
                elif self.visited_grid[r, c] == 1:
                    display += "o"
                else:
                    display += "."
            display += "\n"
        return display


def solve_part_1(input : str) -> int:
    board = Board(input)
    while board.move_guard():
        continue

    return sum(board.visited_grid.flatten())

def solve_part_2(input : str) -> int:
    board = Board(input)
    while board.move_guard():
        continue

    #Get a list of all visited positions
    visited = board.visited_grid == 1
    row_indeces, col_indices = np.where(visited)
    visited_positions = list(zip(row_indeces, col_indices))

    number_of_looping_obstacles = 0

    for position in visited_positions:
        new_board = Board(input)
        new_board.add_obstacle(position)

        new_board.guard.save_current_position()
        loop_detected = False
        while new_board.move_guard():
            if new_board.guard.is_in_known_position():
                loop_detected = True
                break
            new_board.guard.save_current_position()
        
        if loop_detected:
            print(f"Obstacle at {position} causes a loop")
            number_of_looping_obstacles += 1
        else:
            print(f"Obstacle at {position} does not cause a loop")
            
    return number_of_looping_obstacles


if __name__ == "__main__":
    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""" 
    input = import_input(year=2024, day=6)
    print(solve_part_2(input))
