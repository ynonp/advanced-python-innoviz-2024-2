"""
Type Hints find errors before you
"""

# after a parameter, add : and the type
# after the function add -> and then the return type
def twice(x: int) -> int:
    return x * 2


x = input("select a number")
double_x = twice(int(x))
print(f"your number * 2 == {double_x}")

print(f"result = {"hello".upper()}")



