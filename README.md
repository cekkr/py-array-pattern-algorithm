# py-array-pattern-algorithm
A python algorithm able to create a sequential pattern that distances arrays order in the best way possible.

Effectively, this algorithm works.

## Usage example
```python
# Where to test the algorithm
from lib import *
import numpy as np

# The side (and the final dimension) should be always odd
side = 11

arr = generatePatternArray(side ** 2)
print("res: ", arr)

two_dimensional_array = np.array(arr).reshape(side, side)

# This operation is important to improve the right working of the algorithm
two_dimensional_array = invertNdArrayOdds(two_dimensional_array)

print(two_dimensional_array)
```

Result of the final 2 dimensional matrix:
```
[[  0  33 120  17  73  64 104   9  65  41 112]
 [100  60  77  21 116  37   5  96  56  81  32]
 [ 16  69  45 108  28  85  52  92   3  35 118]
 [ 54  83  30 110  43  67  11 102  62  75  19]
 [ 94   8  39 114  23  79  58  98  14  71  47]
 [ 63  74  18 119  34   2  90  50  87  26 106]
 [103  10  66  42 111  31  82  55  95   6  38]
 [ 86  27 107  46  70  15  99  59  78  22 115]
 [ 51  91   4  36 117  20  76  61 101  12  68]
 [ 80  24 113  40   7  93  53  84  29 109  44]
 [ 57  97  13  72  48 105  25  88  49  89   1]]
```

Is it an advantage respect than a random generated array?
I don't know. But it results always the same values given the same input dimension.