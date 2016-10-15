
from pylab import imshow, show
import mahotas
import mahotas.demos
import numpy as np

# Load "Wally" image
wally = mahotas.demos.load('Wally')

# # Image info
# print type(wally)
# print wally.dtype
# print wally.shape
# imshow(wally)
# show()


print wally.dtype
wfloat = wally.astype(float)
print wfloat.dtype



#
# wfloat = wally.astype(float)
# r,g,b = wfloat.transpose((2,0,1))
#
#
# imshow(wally)
# show()