import random


class simpleInsertionSort:
    def __init__(self, size):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 100000))

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 100000))

    def sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while key < self.array[j] and j>=0:
                self.comparisonCount += 1
                self.forwardingCount += 1
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key
            self.forwardingCount += 1

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)




