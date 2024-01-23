import numpy as np

# 1
np.arange(2, 202, 2)

# 2
a = np.arange(1, 11)
b = np.arange(1, 11).reshape(10, 1)
a * b

# 3
np.diag(a * b)

# 4
a = np.random.randint(100, size=10)
a[a % 2 == 1]

# 5
np.where(a % 2 == 1, a, 0)

# 6
a = np.random.randint(100, size=(10,))
np.min(a[a > 50])

# 7
a = np.random.randint(100, size=(100,))
np.sort(np.unique(a))[-5:]



