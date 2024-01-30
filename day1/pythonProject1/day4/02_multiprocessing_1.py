# for processes:
from multiprocessing import Pool

# For threads:
# from multiprocessing.dummy import Pool
import time

def f(x):
    return x*x

# 5 processes = 91848000
# 5 threads =   35383000
# 1 thread =       65000

if __name__ == '__main__':
    t0 = time.time_ns()
    with Pool(5) as p:
        print(sum(p.map(f, range(1_000))))
    t1 = time.time_ns()
    print(f"it took 5 threads {t1 - t0} ns")

    t2 = time.time_ns()
    print(sum(f(i) for i in range(1_000)))
    t3 = time.time_ns()
    print(f"it took 1 thread {t3 - t2} ns")

