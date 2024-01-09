# Where to test the algorithm
from lib import *
import numpy as np

if False:
    size = 2048
    arr = generatePatternArray(size)
    arr = getGradient(arr, size)
    print(arr)

if True:
    # The side (and the final dimension) should be always odd
    side = 11

    arr = generatePatternArray(side ** 2)
    print("res: ", arr)

    two_dimensional_array = np.array(arr).reshape(side, side)
    #two_dimensional_array = invertNdArrayOdds(two_dimensional_array)
    print(two_dimensional_array)

if False:
    for i in range(3, 1001):
        if i%2 == 1:
            arr = generatePatternArray(i)
            print("res: ", arr)