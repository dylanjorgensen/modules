import matplotlib.pyplot as plt
import numpy as np



# Data
x = [0,1,2]
y = [0,1,4]

x_highres = np.linspace(0, 2, 20)
y_highres = x_highres ** 2


# Instantiate
fig = plt.figure()
axes = fig.add_subplot(111)

# Plot: Basic
axes.plot(x, y)
axes.plot(x_highres, y_highres)


# Title and labels
axes.set_title('$y=x^2$') ## Notice you can you LaTeX Code
axes.set_xlabel('x is the best')
axes.set_ylabel('y is very cool')

# Grid
axes.grid()

# Figure size

# Show
plt.show()



