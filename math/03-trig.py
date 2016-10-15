# Resources
# - https://docs.python.org/2/library/math.html

import math
import numpy as np



# --- Constants --- #
math.pi  # pi = 3.141592..., to available precision.
math.e  # e = 2.718281..., to available precision


# --- Trigonometric functions --- #

# Return the Euclidean norm, sqrt(x*x + y*y).
# This is the length of the vector from the origin to point (x, y).
math.hypot(50, 75)


# Sine
math.sin(50)  # Return the sine of x radians.
# math.asin(100)  # Return the arc sine of x, in radians.

# Cosine
math.cos(50)  # Return the cosine of x radians
# math.acos(100)  # Return the arc cosine of x, in radians.

# Tangent
math.tan(50)  # Return the tangent of x radians.
# math.atan(100)  # Return the arc tangent of x, in radians.


# --- Angular conversion --- #

# Converts from radians to degrees
math.degrees(100)  # Convert angle x from radians to degrees.
np.rad2deg(1.57079632679)


# Converts from degrees to radians
math.radians(10)  # Convert angle x from degrees to radians.s
np.deg2rad(180)
np.deg2rad([90,45,30,180])