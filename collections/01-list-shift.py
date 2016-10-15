
from collections import deque

list = [1,2,3,4,5]

def move(list, U):
   p = deque(list)
   p.rotate(U)  # to the right
   return p

print move(list, 1)
print move(list, 3)