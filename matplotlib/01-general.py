# Resources
# - http://nbviewer.ipython.org/github/twistedhardware/mltutorial/blob/master/notebooks/IPython-Tutorial/5%20-%20Plotting%20Charts.ipynb
# - https://www.youtube.com/watch?v=kHPEz1wZZWc
# http://matplotlib.org/gallery.html
# http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut1.html

'''
pylab is part of matplotlib (in matplotlib.pylab) and tries to give you a MatLab like environment. matplotlib has a number of dependencies, among them numpy
'''


import matplotlib.pyplot as plt

# Step1: Define data points
x = [0,1,2]
y = [0,1,4]

# Step2: Instantiate a figure
fig = plt.figure()

# Step3: Best practice is to do all your work inside a subplot
ax = fig.add_subplot(111) # The 111 defines we are working with 1 chart (x,y,first)

# Step4: Plot our data in our subplot
ax.plot(x, y)

# Step5: Generate graph
plt.show()