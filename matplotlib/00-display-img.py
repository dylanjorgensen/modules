
import os

# Get current working directory
print os.getcwd()

# List everything in the directory
print os.listdir(os.curdir)




import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('trash.png')
plt.imshow(img)
plt.show()