# exercise link:
# https://adventofcode.com/2022/day/9
from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int


class Head:
    position: Position

    def move_right(self):
        ...

    def move_left(self):
        ...

    def move_up(self):
        ...

    def move_down(self):
        ...

class Tail:
    position: Position
    head: Head
    visited_positions: set[Position]

    def follow(self):
        ...


instructions = [
    'R', 'R', 'R', 'R',
    'U', 'U', 'U', 'U',
    'L', 'L', 'L',
    'D',
    'R', 'R', 'R', 'R',
    'D',
    'L', 'L', 'L', 'L', 'L',
    'R', 'R'
]

for instruction in instructions:
    ...
