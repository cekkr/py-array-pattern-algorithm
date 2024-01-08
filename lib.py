
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
        return


class PatternArrayBitCount:
    def __init__(self):
        self.bits = []
