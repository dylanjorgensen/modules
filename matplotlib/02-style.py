import matplotlib.pyplot as plt
import numpy as np

'''
==========  ========
character   color
==========  ========
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
==========  ========
'''

# Data
x = [0,1,2]
y = [0,1,4]

x_highres = np.linspace(0, 2, 20)
y_highres = x_highres ** 2


# Figure size
fig = plt.figure(figsize=(12,8))
axes = fig.add_subplot(111)

# Plot: Basic
# axes.plot(x, y)
# axes.plot(x_highres, y_highres)

# Plot: Color and linestyle
axes.plot(x, y, "r--")  # This is shorthand for some of the parameters below
axes.plot(x_highres, y_highres, color="red", linestyle='dashed', linewidth=5, alpha=0.3)

# Plot: Markers identify the original data points
# axes.plot(x, y)
# axes.plot(x_highres, y_highres, marker='o', markerfacecolor='blue', markersize=5)


# Show
plt.show()


