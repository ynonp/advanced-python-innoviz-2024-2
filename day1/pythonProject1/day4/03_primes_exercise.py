import math


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""
Your task:
1. Use multiprocessing module to count the prime numbers
2. Tell me how long it took, try different thread values
3. Try to use multiple processes vs. multiple threads
"""

if __name__ == "__main__":
    print(sum(is_prime(i) for i in range(1_000_000)))