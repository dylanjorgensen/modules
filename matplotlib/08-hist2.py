
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)

fig, ax = plt.subplots()

H = ax.hist(x, bins=50, alpha=0.5, histtype='stepfilled')

plt.show()