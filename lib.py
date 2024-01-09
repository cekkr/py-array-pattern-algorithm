import random
import numpy as np

def generatePatternArray(dim):
    if dim == 2:
        return [0, 1]
    elif dim == 1:
        return [0]

    if dim % 2 == 0:
        print("The dimension should odd")

    arr = [-1] * dim

    '''
    order = []
    for n in range(0, dim):
        order.append(n)

    random.shuffle(order)
    '''

    primaryPoint = PatternArrayPoint(arr, 1)
    status = PatternArrayStatus(dim)
    for l in range(0, primaryPoint.maxLevel+2):
        # Set children
        childrenBitCount = PatternArrayBitCount(l+1)
        while childrenBitCount.next():
            index = childrenBitCount.getNumber()
            #print(index)

            newNum = status.get()
            if status.completed:
                return arr

            #newNum = order[newNum]

            oldNum = primaryPoint.setByIndex(index, newNum)
            if oldNum == -1:
                status.next()

            childrenBitCount.increment()

        # Set point
        children = primaryPoint.getChildrenLevel(l)
        if len(children) > 0:
            levelBitCount = PatternArrayBitCount(l)
            while levelBitCount.next():
                index = levelBitCount.toNumber()
                child = children[index]

                newNum = status.get()
                if status.completed:
                    return arr
                #newNum = order[newNum]

                oldNum = child.set(newNum)
                if oldNum == -1:
                    status.next()

                levelBitCount.increment()

    # Lazy solution
    unset = arr.count(-1)
    if unset > 0:
        order = generatePatternArray(unset)
        res = [0]*unset
        for o in order:
            res[o] = status.curNum
            status.next()

        i = 0
        for a in range(0, dim):
            if arr[a] == -1:
                arr[a] = res[i]
                i += 1

    return arr

class PatternArrayStatus:
    def __init__(self, dim):
        self.curNum = 0
        self.dim = dim
        self.completed = False

    def next(self):
        self.curNum += 1

    def get(self):
        res = self.curNum

        if res >= self.dim:
            self.completed = True

        return res

class PatternArrayPoint:
    def __init__(self, arr, dim, parent=None, childNo=0):
        self.arr = arr
        self.aDim = len(arr)
        self.dim = dim
        self.parent = parent
        self.childNo = childNo

        self.cycle = 0

        if parent is None:
            self.level = 0
        else:
            self.level = parent.level + 1

        self.maxLevel = self.level

        focusDim = self.aDim - 1
        if parent is not None:
            focusDim = parent.pointSize

        self.pointSize = focusDim / 2
        self.pointPos = self.pointSize

        if self.parent is not None:
            self.pointPos = parent.pointPos + (self.pointSize * childNo)

        #print(self.pointPos, self.pointSize)

        self.numChildren = 0
        self.children = None
        if self.pointSize >= 1:
            self.calculateChildren()

    def countChildren(self, add, level=0):
        self.numChildren += add

        if level > self.maxLevel:
            self.maxLevel = level

        if self.parent is not None:
            self.parent.countChildren(add, self.maxLevel)

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
            child = self.getChild(index, len(children))

            # I do that because I don't know how it can continue the algorithm...
            if child is not None:
                children.append(child)

            bitCount.increment()

        return children

    def getChild(self, index, lev=-1):
        lenIndex = len(index)

        if lenIndex == 0:
            return self

        if self.children is None:
            return None

        myI = index[0]

        if lev == -1:
            self.cycle += 1
            lev = self.cycle

        '''
        if lev % 2 == 0 and False:
            myI = 0 if myI == 1 else 1
        '''

        return self.children[myI].getChild(index[1:])

    def set(self, n, p=0):
        pos = int(self.pointPos + (self.pointSize * p))

        oldNum = self.arr[pos]

        if oldNum != -1:
            return oldNum

        self.arr[pos] = n

        return oldNum

    def setByIndex(self, index, n):
        child = self.getChild(index)

        if child is None:
            return False

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


def invertNdArrayOdds(arr):
    # Determine the shape of the firsts arrays
    firstShapes = arr.shape[:-1]

    for count, index in enumerate(np.ndindex(firstShapes)):
        if count % 2 == 1:
            arr[index] = np.flip(arr[index])

    return arr

def getGradient(arr, dim):
    for i in range(0, len(arr)):
        arr[i] = arr[i]/(dim-1)
    return arr