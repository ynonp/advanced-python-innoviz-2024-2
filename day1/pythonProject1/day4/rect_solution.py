"""
Solution of: https://adventofcode.com/2016/day/8
"""
import numpy as np

class Screen:
    def __init__(self):
        self.screen = np.zeros((6, 50), dtype=bool)

    def __str__(self):
        return '\n'.join(
            [''.join(np.where(self.screen, "#", ".")[n])
             for n in range(len(self.screen))])

    def rect(self, columns: int, rows: int):
        self.screen[:rows, :columns] = True

    def rotate_column(self, column: int, by: int):
        self.screen[:, column] = np.roll(self.screen[:, column], by)

    def rotate_row(self, row: int, by: int):
        self.screen[row] = np.roll(self.screen[row], by)

if __name__ == "__main__":
    s = Screen()
    with open('input.txt', encoding='utf8') as f:
        for line in f:
            match line.split():
                # rect 1x1
                case ["rect", size]:
                    columns, rows = size.split("x")
                    s.rect(int(columns), int(rows))

                # rotate row y=0 by 5
                case ["rotate", "row", y, "by", by]:
                    _, row = y.split("=")
                    s.rotate_row(int(row), int(by))

                # rotate column x=30 by 1
                case ["rotate", "column", x, "by", by]:
                    _, col = x.split("=")
                    s.rotate_column(int(col), int(by))

                case _:
                    print(f"Unrecognized line: {line}")

    print(f"There are {np.sum(s.screen)} lit pixels")
    print(s)
