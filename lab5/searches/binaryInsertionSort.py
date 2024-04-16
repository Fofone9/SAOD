import random


class binaryInsertionSort:
    def __init__(self):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.array = list()

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 10))

    def binarySearch(self, target, end):
        l = 0
        r = end
        if target >= self.array[end-1]:
            return end
        while l < r:
            self.comparisonCount += 1
            m = (l+r)//2
            if self.array[m] == target:
                return m
            elif self.array[m] > target:
                r = m-1
            else:
                l = m+1
        self.comparisonCount += 1
        if r <= 0 and self.array[0] >= target:
            return 0
        elif self.array[r-1] < target and self.array[r] >= target:
            return r
        else:
            return r+1

    def sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            startPosition = self.binarySearch(key, i)
            for j in range(startPosition, i+1):
                self.forwardingCount += 1
                temp = self.array[j]
                self.array[j] = key
                key = temp

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)



