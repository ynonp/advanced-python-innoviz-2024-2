import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(1, 100)
x = np.arange(1, 101)
y = x ** 2
df = pd.DataFrame   (data=[x, y]).transpose()
df.columns = ['x', 'x^2']

df.plot()
plt.show()

