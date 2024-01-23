# Let's implement the game Mastermind
# and play against the computer
# First play a bit online:
# https://www.archimedes-lab.org/mastermind.html
#
# Create a python program that helps me win this game
#
# Your program suggests a move
# I tell the program the results I got (whites and blacks)
# Your program suggests the next move
# and so on until we win

# ynon@ynonperek.com
from dataclasses import dataclass
import itertools

color = {
    '1': 'Red',
    '2': 'Green',
    '3': 'Purple',
    '4': 'Yellow',
    '5': 'Brown',
    '6': 'Orange',
    '7': 'Black',
    '8': 'White'
}

@dataclass(frozen=True)
class Result:
    whites: int
    blacks: int


class GameNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ' '.join([color[ch] for ch in str(self.value)])

    def __repr__(self):
        return str(self.value)

    def compare(self, other: "GameNumber") -> Result:
        blacks = 0
        whites = 0
        for idx1, i in enumerate(str(self.value)):
            for idx2, j in enumerate(str(other.value)):
                if i == j:
                    if idx1 == idx2:
                        blacks += 1
                    else:
                        whites += 1
        return Result(blacks=blacks, whites=whites)


class GameSolver:
    def __init__(self):
        self.possible_solutions = [
            GameNumber(int(''.join(str(c) for c in p)))
            for p in itertools.permutations(range(1, 9), 4)
        ]

    def suggest_guess(self) -> GameNumber:
        return self.possible_solutions[0]

    def check_result(self, result: Result):
        guess = self.suggest_guess()
        self.possible_solutions = [
            v for v in self.possible_solutions
            if v.compare(guess) == result]


if __name__ == "__main__":
    game_solver = GameSolver()
    while True:
        print(game_solver.suggest_guess())
        result_str = input("result? ")
        whites, blacks = [int(x) for x in result_str.split()]
        result = Result(whites=whites, blacks=blacks)
        game_solver.check_result(result)

# for next_suggestion in game_solver:
#     # now I got online and try the next suggestion
#     game_solver.results(white=3, black=1)









