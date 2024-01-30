import math
import multiprocessing as mpp
import multiprocessing.dummy as mpt
import time

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

"""
1 thread -   2195738000
8 threads -  2093909000
8 processes - 529401000
"""

if __name__ == "__main__":
    t0 = time.time_ns()
    print(sum(is_prime(i) for i in range(1_000_000)))
    t1 = time.time_ns()

    pool_threads = mpt.Pool(8)
    t2 = time.time_ns()
    print(sum(pool_threads.map(is_prime, range(1_000_000))))
    t3 = time.time_ns()

    pool_processes = mpp.Pool(8)
    t4 = time.time_ns()
    print(sum(pool_processes.map(is_prime, range(1_000_000))))
    t5 = time.time_ns()

    print(f"1 thread - {t1 - t0}")
    print(f"8 threads - {t3 - t2}")
    print(f"8 processes - {t5 - t4}")






