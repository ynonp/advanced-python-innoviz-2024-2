def sum_squares(*numbers: int) -> list[int]:
    return [n * n for n in numbers]


print(sum_squares(10, 12, 15))
sum_squares(*range(50))


