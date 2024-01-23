from day2.exercise import GameNumber, GameSolver, Result

def test_some_numbers1():
    n1 = GameNumber(1234)
    n2 = GameNumber(1256)
    result = n1.compare(n2)
    assert result.whites == 0
    assert result.blacks == 2

def test_compare_with_doubles():
    n1 = GameNumber(1112)
    n2 = GameNumber(2221)
    result = n1.compare(n2)
    assert result.whites == 0
    assert result.blacks == 2


def test_some_numbers2():
    n1 = GameNumber(1234)
    n2 = GameNumber(5678)
    result = n1.compare(n2)
    assert result.whites == 0
    assert result.blacks == 0


def test_some_numbers3():
    n1 = GameNumber(1234)
    n2 = GameNumber(1234)
    result = n1.compare(n2)
    assert result.whites == 0
    assert result.blacks == 4


def test_to_string():
    n1 = GameNumber(1234)
    assert n1.__str__() == "Blue Green Orange Purple"

def test_possible_options():
    game_solver = GameSolver()
    assert game_solver.suggest_guess().value == 1234


def test_reduce_options():
    game_solver = GameSolver()
    guess = game_solver.suggest_guess()
    game_solver.check_result(Result(whites=2, blacks=0))
    for i in game_solver.possible_solutions:
        assert i.compare(guess).whites == 2
        assert i.compare(guess).blacks == 0

    print(game_solver.possible_solutions)


def test_second_guess():
    game_solver = GameSolver()
    guess = game_solver.suggest_guess()
    game_solver.check_result(Result(whites=2, blacks=0))
    print(game_solver.suggest_guess())
