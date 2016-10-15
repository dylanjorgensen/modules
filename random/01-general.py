# Resources
# - https://docs.python.org/2/library/random.html
# - http://www.tutorialspoint.com/python/number_seed.htm

import random


# seed() sets the integer starting value used in generating random numbers. Call this function before calling any other random module function.
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()





