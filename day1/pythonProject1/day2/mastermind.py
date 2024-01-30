import itertools
from dataclasses import dataclass

color = {
    '1': 'Blue',
    '2': 'Green',
    '3': 'Orange',
    '4': 'Purple',
    '5': 'Red',
    '6': 'Yellow',
}

@dataclass(frozen=True)
class Result:
    white: int
    black: int

class Guess:
    def __init__(self, value: int):
        self.string = ' '.join([color[ch] for ch in str(value)])

        digitgroups = itertools.groupby(
            sorted(list(enumerate(str(value))), key=lambda m: m[1]),
            lambda m: m[1])

        self.value = {
            k: set([i[0] for i in v])
            for k, v in digitgroups
        }

    def compare(self, other: "Guess") -> Result:
        white = 0
        black = 0
        for digit in self.value.keys():
            if digit in other.value:
                intersection = self.value[digit].intersection(other.value[digit])
                black += len(intersection)
                white += min(len(self.value[digit] - intersection), len(other.value[digit] - intersection))

        return Result(white=white, black=black)

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.string

class GameSolver:
    def __init__(self):
        self.possible_solutions = [
            Guess(int(''.join(str(c) for c in p)))
            for p in itertools.product(range(1, 7), range(1, 7), range(1, 7), range(1, 7))
        ]

    def suggest_guess(self) -> Guess:
        return self.possible_solutions[0]

    def check_result(self, result: Result):
        guess = self.suggest_guess()
        self.possible_solutions = [
            v for v in self.possible_solutions
            if v.compare(guess) == result]


if __name__ == "__main__":
    game_solver = GameSolver()
    # while True:
    #     print(game_solver.suggest_guess())
    #     result_str = input("result? ")
    #     whites, blacks = [int(x) for x in result_str.split()]
    #     result = Result(white=whites, black=blacks)
    #     game_solver.check_result(result)

    g1 = Guess(112)
    g2 = Guess(221)
    print(g1.compare(g2))