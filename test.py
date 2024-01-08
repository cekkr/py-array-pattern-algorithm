# Where to test the algorithm
from lib import *

for i in range(3, 1001):
    if i%2 == 1:
        arr = generatePatternArray(i)
        print("res: ", arr)