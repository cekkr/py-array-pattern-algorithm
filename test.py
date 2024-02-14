# Where to test the algorithm
from lib import *
import numpy as np

if False:
    from scipy.fft import fft, fftfreq
    import matplotlib.pyplot as plt

    size = 3 ** 10
    arr = generatePatternArray(size)
    arr = getGradient(arr, size)
    arr = [x - 0.5 for x in arr]

    N = size
    T = 1
    yf = fft(arr)
    xf = fftfreq(N, T)[:N // 2]

    plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
    plt.grid()
    plt.show()

if True:
    # The side (and the final dimension) should be always odd
    side = 7

    size = side ** 2

    arr = generatePatternArray(size)
    print("res: ", arr)

    two_dimensional_array = np.array(arr).reshape(side, side)
    two_dimensional_array = invertNdArrayOdds(two_dimensional_array)
    print(two_dimensional_array)

    #arr = two_dimensional_array.reshape(side ** 2)

    # Calculate by index

    array_index = np.zeros(size)    
    for i in range(0, size):
        array_index[arr[i]] = i

    print("")
    print("by index:")
    print(array_index.reshape(side, side))

    # Calculate by gradient
    array_gradient = np.zeros((size,2))
    sideMinus = side - 1
    for i in range(0, size):
        val = arr[i]
        x = (val % side)/sideMinus
        y = round(val / sideMinus) / (sideMinus*2)
        array_gradient[i] = [x, y]

    #array_gradient = array_gradient.reshape(side, side)

    print("")
    print("by gradient:")
    print(array_gradient)



    '''
    array_index = np.zeros(side ** 2)
    for i in range(0, size):
        array_index[i] = 
    '''

if False:
    for i in range(3, 1001):
        if i%2 == 1:
            arr = generatePatternArray(i)
            print("res: ", arr)