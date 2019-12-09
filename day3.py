# day 3
from typing import Tuple, List, Set, Dict
from dataclasses import dataclass

def manhattan(x: Tuple[int, int], y:Tuple[int, int]) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def parse_instruction(instruction: str) -> Tuple[str, int]:
    direction = instruction[0]
    move = int(instruction[1:])
    return (direction, move)
    
def move(instruction: str, cursor: Tuple[int,int]):
    direction, move = parse_instruction(instruction)   
    x, y = cursor
    if direction == 'R':
        cursor = (x+move,y)
        points = [(x+i, y) for i in range(move)]
    elif direction == 'L':
        cursor = (x-move,y)
        points = [(x-i, y) for i in range(move)]
    elif direction == 'U':
        cursor = (x,y+move)
        points = [(x, y+i) for i in range(move)]
    elif direction == 'D':
        cursor = (x,y-move)
        points = [(x, y-i) for i in range(move)]

    return points, cursor


@dataclass
class Wire:
    instructions: List[str]
    points: Set[Tuple[int,int]]
    step_counter: Dict

    def build_path(self):
        """construct path from wire instructions"""
        cursor = (0,0)
        counter = 0
        for instruction in self.instructions:
            points, cursor = move(instruction, cursor)
            for point in points:
                self.points.add(point)
                self.step_counter[point] = counter
                counter += 1
        

if __name__ == "__main__":   

    # wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    # wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

    with open('day3_input.txt') as input:
        lines = input.readlines()
        [wire1, wire2] = [line.replace('\n','').split(',') for line in lines]

    w1 = Wire(wire1, {(0,0)}, {})
    w2 = Wire(wire2, {(0,0)}, {})

    w1.build_path()
    w2.build_path()

    intersections = w1.points & w2.points
    intersections.remove((0,0))
    
    # part1
    print(min(manhattan((0,0),i) for i in intersections))

    # part2
    print(min(w1.step_counter[point] + w2.step_counter[point] for point in intersections))