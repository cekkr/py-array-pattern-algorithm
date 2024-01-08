
def generatePatternArray(dim):
    if dim % 2 == 0:
        raise Exception("The dimension should uneven")

    arr = [-1] * dim

    primaryPoint = PatternArrayPoint(arr, 1)

    status = PatternArrayStatus()
    primaryPoint.calculate(status)

    return arr

class PatternArrayStatus:
    def __init__(self):
        self.level = 0
        self.curNum = 0

    def newLevel(self):
        self.level += 1
        self.bitCount = PatternArrayBitCount()

class PatternArrayPoint:
    def __init__(self, arr, dim, parent=None, childNo=0):
        self.arr = arr
        self.aDim = len(arr)
        self.dim = dim
        self.parent = parent
        self.childNo = childNo

        if parent is None:
            self.level = 1
        else:
            self.level = parent.level + 1

        self.pointSize = (self.aDim / dim) / 2
        self.pointPos = self.aDim - self.pointSize

        if self.parent is not None:
            self.pointPos = parent.pointPos + (self.pointPos * childNo)

        self.numChildren = 0
        self.children = None
        if self.pointSize > 1:
            self.calculateChildren()

    def countChildren(self, add):
        self.numChildren += add
        if self.parent is not None:
            self.parent.countChildren(add)

    def calculateChildren(self):
        self.childLeft = PatternArrayPoint(self.arr, self.dim + 1, self, -1)
        self.childRight = PatternArrayPoint(self.arr, self.dim + 1, self, 1)

        self.children = [self.childLeft, self.childRight]
        self.countChildren(2)

    def calculate(self, status):
        status.newLevel()
        status.bitCount.deeper()

        while not status.bitCount.next():
            index = status.bitCount.getIndex()
            num = status.curNum + status.bitCount.toNumber()
            self.set(index, num)
            status.bitCount.increment()

        status.curNum += (2 ** status.bitCount.nBits)
        self.set([], status.curNum)
        status.curNum += 1

        nextChildren = self.getNextChildren()
        if len(nextChildren) > 0:
            return

    def getNextChildren(self):
        children = []
        bitCount = PatternArrayBitCount(self.level)
        while not bitCount.next():
            child = self.getChild(bitCount.bits)

            # I do that because I don't know how it can continue the algorithm...
            if child is not None:
                children.append(child)

            bitCount.increment()

        return children

    def getChild(self, index):
        lenIndex = len(index)

        if lenIndex == 0:
            return self

        if self.children is None:
            return None

        myI = 0
        if lenIndex == 1:
            myI = -1 if index[0] == 0 else 1

        return self.children[myI].getChild(index[1:])

    def set(self, index, n):
        lenIndex = len(index)

        myI = 0
        if lenIndex == 1:
            myI = -1 if index[0] == 0 else 1

        if lenIndex > 1:
            self.children[myI].set(index[1:], n)
        else:
            pos = self.pointPos + (self.pointSize * myI)
            self.arr[pos] = n

def bits_to_number(bit_list):
    decimal_number = 0
    for bit in bit_list:
        decimal_number = decimal_number * 2 + bit
    return decimal_number

class PatternArrayBitCount:
    def __init__(self, length=0):
        self.nBits = length
        self.bits = [0] * length

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

    def next(self):
        return self.bits[0] > 1

    def getIndex(self):
        return self.bits[::-1]

    def toIndex(self):
        bit_list = self.bits[::-1]
        return bits_to_number(bit_list)

    def toNumber(self):
        bit_list = self.bits

        if bit_list[0] == 1:
            bit_list = bit_list[::-1]

        return bits_to_number(bit_list)
