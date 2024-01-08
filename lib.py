
def generatePatternArray(dim):
    if dim % 2 == 0:
        raise Exception("The dimension should uneven")

    arr = [-1] * dim

    primaryPoint = PatternArrayPoint(arr, 1)
    status = PatternArrayStatus()
    for l in range(0, primaryPoint.maxLevel+2):
        status.newLevel()
        children = primaryPoint.getChildrenLevel(l)

        # Set children
        childrenBitCount = PatternArrayBitCount(l+1)
        while childrenBitCount.next():
            index = childrenBitCount.getNumber()
            print("index = ",index)
            if primaryPoint.setByIndex(index, status.curNum):
                status.next()
                print("1. num: ", status.curNum)
            else:
                print("repeat set occours 1")

            childrenBitCount.increment()

        # Set point
        levelBitCount = PatternArrayBitCount(l)
        while levelBitCount.next():
            index = levelBitCount.toIndex()
            child = children[index]

            if child.set(status.curNum):
                status.next()
                print("2. num: ", status.curNum)
            else:
                print("repeat set occours 2")

            levelBitCount.increment()

    return arr

class PatternArrayStatus:
    def __init__(self):
        self.level = 0
        self.curNum = 0

    def newLevel(self):
        self.level += 1

    def next(self):
        self.curNum += 1

class PatternArrayPoint:
    def __init__(self, arr, dim, parent=None, childNo=0):
        self.arr = arr
        self.aDim = len(arr)
        self.dim = dim
        self.parent = parent
        self.childNo = childNo

        if parent is None:
            self.level = 0
        else:
            self.level = parent.level + 1

        self.maxLevel = 0

        focusDim = self.aDim - 1
        if parent is not None:
            focusDim = parent.pointSize - 1

        self.pointSize = focusDim / (2 ** dim)
        self.pointPos = focusDim - self.pointSize

        if self.parent is not None:
            self.pointPos = parent.pointPos + (self.pointSize * childNo)

        self.numChildren = 0
        self.children = None
        if self.pointSize > 1:
            self.calculateChildren()

    def countChildren(self, add, level=0):
        self.numChildren += add

        if level > self.maxLevel:
            self.maxLevel = level

        if self.parent is not None:
            self.parent.countChildren(add, self.level)

    def calculateChildren(self):
        self.childLeft = PatternArrayPoint(self.arr, self.dim + 1, self, -1)
        self.childRight = PatternArrayPoint(self.arr, self.dim + 1, self, 1)

        self.children = [self.childLeft, self.childRight]
        self.countChildren(2)

    def getChildrenLevel(self, level):
        children = []

        bitCount = PatternArrayBitCount(level)
        while bitCount.next():
            index = bitCount.getIndex()
            child = self.getChild(index)

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

        myI = index[0]
        return self.children[myI].getChild(index[1:])

    def set(self, n, p=0):
        pos = int(self.pointPos + (self.pointSize * p))
        if self.arr[pos] == -1:
            self.arr[pos] = n
            return True

        return False

    def setByIndex(self, index, n):
        child = self.getChild(index[:-1])
        myI = -1 if index[-1] == 0 else 1
        return child.set(n, myI)


def bits_to_number(bit_list):
    decimal_number = 0
    for bit in bit_list:
        decimal_number = decimal_number * 2 + bit
    return decimal_number

class PatternArrayBitCount:
    def __init__(self, length=0):
        self.nBits = length
        self.bits = [0] * length
        self.done = False

    def deeper(self):
        self.nBits += 1
        self.bits = [0] * self.nBits

    def increment(self):
        if self.nBits == 0 or all(x == 1 for x in self.bits):
            self.done = True
            return

        self.bits[self.nBits-1] += 1

        acc = 0
        for i in range(self.nBits-1, -1, -1):
            self.bits[i] += acc
            acc = 0

            if self.bits[i] > 1:
                acc = 1
                self.bits[i] = 0

        return self.bits

    def next(self):
        return not self.done

    def getIndex(self):
        return self.bits[::-1]

    def getNumber(self):
        if self.nBits == 0:
            return []

        bit_list = self.bits[:]

        if bit_list[0] == 1:
            for i in range(1, self.nBits):
                bit_list[i] = 1 if bit_list[i] == 0 else 0

        return bit_list

    def toIndex(self):
        bit_list = self.getIndex()
        return bits_to_number(bit_list)

    def toNumber(self):
        bit_list = self.getNumber()
        return bits_to_number(bit_list)
