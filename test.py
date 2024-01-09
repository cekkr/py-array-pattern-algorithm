# Where to test the algorithm
from lib import *
import numpy as np

side = 7

arr = generatePatternArray(10 ** 2)
print("res: ", arr)

two_dimensional_array = np.array(arr).reshape(10, 10)
print(two_dimensional_array)

exit(0)

for i in range(3, 1001):
    if i%2 == 1:
        arr = generatePatternArray(i)
        print("res: ", arr)