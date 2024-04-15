import random


class simpleInsertionSort:
    def __init__(self):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.array = list()

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 100000))

    def sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while key < self.array[j] and j>=0:
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()


test = simpleInsertionSort()
test.setArray(10)
test.show()
test.sort()
test.show()
