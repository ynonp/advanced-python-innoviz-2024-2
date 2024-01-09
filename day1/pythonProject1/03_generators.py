"""
Fib is a generator because it uses yield
"yield" yields a value, that is consumed with "next"
"""
def fib():
    a, b = 1, 1
    while True:
        a, b = b, a + b
        yield a

"""
Using Generators

1. Call the generator function and use next(g) with the result object
"""
g = fib()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

"""
2. You can use a generator inside a "for" loop
"""

for i in fib():
    print(i)
    if i > 100:
        break


"""
3. Python has many built-in functions to work with generators
   in the module itertools
"""

import itertools

for i in itertools.takewhile(lambda x: x < 100, fib()):
    print(i)


"""
4. Generator comprehension is cool and might go unnoticed
"""

# Create a list and print its sum
print(sum([i * i for i in range(100)]))

# Create a generator and print its sum (saving memory)
print(sum((i * i for i in range(100))))

# Create a generator and print its sum (saving memory),
# shorter syntax
print(sum(i * i for i in range(100)))



#
#
# print(fib(5))
# print(sum([fib(i) for i in range(100)]))
