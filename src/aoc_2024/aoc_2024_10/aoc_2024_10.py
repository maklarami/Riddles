# Advent of Code 2024 - Day 10 solution

import numpy as np

class Map:
    def __init__(self, input: str):
        self.grid = np.array([[int(char) for char in line] for line in input.splitlines()])
        self.size = self.grid.shape
        print(self.size)

    def __repr__(self):
        return "\n".join("".join(map(str, line)).join("\n") for line in self.grid)
    
    def find_positions(self, value):
        rows, cols = np.where(self.grid == value)
        return list(zip(rows, cols))
    
    def path_possonibilities(self, position):
        value = self.grid[position]
        possibilities = [(position[0]+1, position[1]), (position[0]-1, position[1]), (position[0], position[1]+1), (position[0], position[1]-1)]
        possibilities = [pos for pos in possibilities if 0 <= pos[0] < self.size[0] and 0 <= pos[1] < self.size[1]]
        possibilities = [pos for pos in possibilities if self.grid[pos] == value + 1]
        return possibilities
        

    def find_path_step(self, paths_peaks: tuple[list, set]) -> tuple[list, set]:
        paths, peaks = paths_peaks
        new_paths = []
        for i, path in enumerate(paths[::-1]):
            position = path[-1]
            value = self.grid[position]

            if value == 9:  # Reached the peak
                peaks.add(position)
                new_paths.append(path)
                continue

            possibilities = self.path_possonibilities(position)
            continues = False

            for possibility in possibilities:
                if not continues:
                    path.append(possibility)
                    continues = True
                else:
                    # Create a new path for the additional possibility
                    new_path = path[:-1] + [possibility]
                    new_paths.append(new_path)         
            
            if continues:
                new_paths.append(path)

        return new_paths, peaks


def solve_part_1(input : str) -> int:
    map = Map(input)
    trailheads = map.find_positions(0)
    scores = []
    for trailhead in trailheads:
        paths = [[trailhead]]
        peaks = set()
        while paths:
            paths, peaks = map.find_path_step((paths, peaks))
        scores.append(len(peaks))
    
    return sum(scores)

def solve_part_2(input : str) -> int:
    map = Map(input)
    trailheads = map.find_positions(0)
    rating = []
    for trailhead in trailheads:
        paths = [[trailhead]]
        peaks = set()
        for _ in range(10):
            paths, peaks = map.find_path_step((paths, peaks))
        rating.append(len(paths))
    
    return sum(rating)

if __name__ == "__main__":
    print(solve_part_2("""0123
1234
8765
9876"""))