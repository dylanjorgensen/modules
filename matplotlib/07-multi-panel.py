# Resources
# - http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut2.html#

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 1000)

# Generates multiple sub-plots
fig = plt.figure()
for i in range(6):
    ax = fig.add_subplot(2, 3, i + 1)
    ax.set_title("Plot #%i" % i)

# Stops the text from overlapping
fig.subplots_adjust(wspace=0.3, hspace=0.3)

# Plot the data on multiple sub plots
for i in range(6):
    fig.axes[i].plot(x, np.sin(i * x))

# Customize Axes Limits
plt.xlim(5, 30)
plt.ylim(-3.2, 1.2)

# Generate graph
plt.show()
