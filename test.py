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
    side = 9

    arr = generatePatternArray(side ** 2)
    print("res: ", arr)

    two_dimensional_array = np.array(arr).reshape(side, side)
    two_dimensional_array = invertNdArrayOdds(two_dimensional_array)
    print(two_dimensional_array)

if False:
    for i in range(3, 1001):
        if i%2 == 1:
            arr = generatePatternArray(i)
            print("res: ", arr)