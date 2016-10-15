# What I learned...
# - We need to import mpl_toolkits.mplot3d for 3D renderings even though we don't call it explicitly in the code .


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


# Instantiate figure and axis
fig = plt.figure()
ax = fig.gca(projection='3d')  # This is why we imported mpl_toolkits.mplot3d

# Generate data
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5

# plot
ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')

# Styles
colors = ('r', 'g', 'b', 'k')
for c in colors:
    x = np.random.sample(20)
    y = np.random.sample(20)
    ax.scatter(x, y, 0, zdir='y', c=c)

# Labels
ax.legend()
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 1)

# Render
plt.show()