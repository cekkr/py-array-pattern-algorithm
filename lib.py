
def generatePatternArray(dim):
    if dim % 2 == 0:
        raise Exception("The dimension should uneven")

    arr = [-1] * dim

    primaryPoint = PatternArrayPoint(arr, 1)

    bitCount = PatternArrayBitCount()
    primaryPoint.calculate(bitCount)

    return arr

class PatternArrayPoint:
    def __init__(self, arr, dim, parent=None, childNo=0):
        self.arr = arr
        self.aDim = len(arr)
        self.dim = dim
        self.parent = parent
        self.childNo = childNo

        self.pointSize = (self.aDim / dim) / 2
        self.pointPos = self.aDim - self.pointSize

        if self.parent is not None:
            self.pointPos = parent.pointPos + (self.pointPos * childNo)

        self.children = None
        if self.pointSize > 1:
            self.calculateChildren()

    def calculateChildren(self):
        self.childLeft = PatternArrayPoint(self.arr, self.dim + 1, self, -1)
        self.childRight = PatternArrayPoint(self.arr, self.dim + 1, self, 1)

        self.children = [self.childLeft, self.childRight]

    def calculate(self, bitCount):
        bitCount.deeper()

        while not bitCount.increment():
            return


class PatternArrayBitCount:
    def __init__(self):
        self.nBits = 0
        self.bits = []

    def deeper(self):
        self.nBits += 1
        self.bits = [0] * self.nBits

    def increment(self):
        self.bits[self.nBits-1] += 1

        acc = 0
        for i in range(self.nBits-1, -1, -1):
            self.bits[i] += acc

            if self.bits[i] > 1:
                acc = 1
                self.bits[i] = 0

        return self.bits[0] > 1
