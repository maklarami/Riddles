# Advent of Code 2024 - Day 08 solution
from enum import Enum
import itertools
import numpy as np

class NodeCalculationModel(Enum):
    PART_1 = "part_1"
    PART_2 = "part_2"

class Layer:
    def __init__(self, antenas: list[np.array]):
        self.antenas = antenas
        self.map = None

    def calculate_nodes_model_1(self) -> set:
        nodes : set[tuple[int, int]] = set()
        for (first, second) in itertools.combinations(self.antenas, 2):
            distance = second - first
            node1 = second + distance
            if self.map.is_within_map(node1):
                nodes.add(tuple(node1))
            node2 = first - distance
            if self.map.is_within_map(node2):
                nodes.add(tuple(node2))
        return nodes
    
    def calculate_nodes_model_2(self) -> set:
        nodes : set[tuple[int, int]] = set()
        for (first, second) in itertools.combinations(self.antenas, 2):
            nodes.add(tuple(second))
            nodes.add(tuple(first))
            distance = second - first

            node = second + distance
            while self.map.is_within_map(node):
                nodes.add(tuple(node))
                node += distance

            node = first - distance
            while self.map.is_within_map(node):
                nodes.add(tuple(node))
                node -= distance

        return nodes

class Map:
    def __init__(self, x :int , y : int):
        self.size = (x,y)
        self.layers = []
        self.nodes = set()

    def add_layer(self, layer : Layer):
        layer.map = self
        self.layers.append(layer)

    def is_within_map(self, node: tuple[int, int]) -> bool: 
        if all(node < self.size) and all (node >= (0,0)):
            return True
        return False
    
    def calculate_nodes(self, model: NodeCalculationModel):
        for layer in self.layers:
            if model == NodeCalculationModel.PART_1:
                self.nodes |= layer.calculate_nodes_model_1()
            elif model == NodeCalculationModel.PART_2:
                self.nodes |= layer.calculate_nodes_model_2()
            else:
                raise ValueError(f"Unknown model: {model}")
            
    def plot_nodes(self) -> str:
        grid = np.full(self.size, '.')

        for node in self.nodes:
            grid[node] = 'X'

        return '\n'.join(''.join(row) for row in grid)

def create_map(input : str) -> Map:
    chars = {}
    antenna_locations : list[tuple[int, int]] = []
    i = 0
    map = None

    for x, line in enumerate(input.splitlines()):
        if x == 0:
            map = Map(len(input.splitlines()), len(line.strip()))
        for y, char in enumerate(line.strip()):
            if char == '.':
                continue
            if char not in chars:
                chars[char] = i
                i += 1
                antenna_locations.append([np.array((x,y))])
            else:
                antenna_locations[chars[char]].append(np.array((x,y)))

    for antenna_set in antenna_locations:
        map.add_layer(Layer(antenna_set))

    return map

def solve_part_1(input : str) -> int:
    map = create_map(input)
    map.calculate_nodes(NodeCalculationModel.PART_1)

    return len(map.nodes)

def solve_part_2(input : str) -> int:
    map = create_map(input)
    map.calculate_nodes(NodeCalculationModel.PART_2)
    print(map.plot_nodes())
    return len(map.nodes)

if __name__ == "__main__":
    pass
