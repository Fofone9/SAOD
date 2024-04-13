import random
class distributiveCountingSort:
    def __init__(self):
        self.size = 0
        self.array = list()

    def setArray(self, size):
        self.array = list()
        self.size = size
        for i in range(size):
            self.array.append(random.randint(10, 25))

    def sort(self):
        minMax = self.getMinMax()
        minKey = minMax[0]
        maxKey = minMax[1]
        n = maxKey-minKey+1
        support = [0 for i in range(n)]
        for element in self.array:
            support[element-minKey] += 1
        size = self.size
        for i in range(n-1, -1, -1):
            size -= support[i]
            support[i] = size
        result = [0 for i in range(self.size)]
        for elem in self.array:
            result[support[elem-minKey]] = elem
            support[elem-minKey] += 1
        self.array = result

    def getMinMax(self):
        return(min(self.array), max(self.array))

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()


test = distributiveCountingSort()
test.setArray(10)
test.show()
test.sort()
test.show()