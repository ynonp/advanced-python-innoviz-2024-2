# exercise link:
# https://adventofcode.com/2022/day/9
from dataclasses import dataclass
from functools import reduce
@dataclass(frozen=True)
class Position:
    x: int = 0
    y: int = 0


class Head:
    position: Position = Position(0, 0)

    def move_right(self):
        self.position = Position(
            y=self.position.y,
            x=self.position.x + 1
        )

    def move_left(self):
        self.position = Position(
            y=self.position.y,
            x=self.position.x - 1
        )

    def move_up(self):
        self.position = Position(
            y=self.position.y - 1,
            x=self.position.x
        )

    def move_down(self):
        self.position = Position(
            y=self.position.y + 1,
            x=self.position.x
        )


class Tail:
    position: Position = Position(0, 0)
    head: Head

    def __init__(self, head):
        self.head = head
        self.visited_positions = set()
        self.visited_positions.add(Position(0, 0))

    def follow(self):
        hx = self.head.position.x
        hy = self.head.position.y
        x = self.position.x
        y = self.position.y
        new_x = x
        new_y = y

        if abs(hx - x) <= 1 and abs(hy - y) <= 1:
            return

        if x < hx:
            new_x += 1
        elif x > hx:
            new_x -= 1

        if y < hy:
            new_y += 1
        elif y > hy:
            new_y -= 1

        self.position = Position(x=new_x, y=new_y)
        self.visited_positions.add(self.position)


def read_instructions_from_file(filename):
    with open(filename, encoding='utf8') as f:
        instructions = [d * int(t)
         for d, t in (line.split() for line in f)]
        instructions = ''.join(instructions)
        instructions = list(instructions)
        return instructions

instructions = read_instructions_from_file('input.txt')
h = Head()
t = Tail(h)


# Next Exercise:
# Need to support longer ropes - a rope of 10 knots!
# Head + tail1 + tail2 + tail3 + ... + tail9
# How many positions did tail9 visit?
rope = reduce(
    lambda rope, _: rope + [Tail(rope[-1])],
    range(9),
    [Head()]
)
print(rope)

h = rope[0]

for instruction in instructions:
    match instruction:
        case "R": h.move_right()
        case "L": h.move_left()
        case "U": h.move_up()
        case "D": h.move_down()

    for knot in rope[1:]:
        knot.follow()

print(len(rope[-1].visited_positions))