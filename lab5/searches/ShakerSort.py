import random


class bubbleSort:
    def __init__(self):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.array = list()
        self.size = 0

    def setArray(self, size):
        self.array = list()
        self.size = size
        for i in range(size):
            self.array.append(random.randint(0, 100000))

    def sort(self):
        a = 0
        b = self.size
        while b != 1:
            t = 0
            y = self.size
            for i in range(a, b-1):
                self.comparisonCount += 1
                if self.array[i] > self.array[i+1]:
                    self.forwardingCount += 1
                    self.array[i], self.array[i + 1] = self.array[i+1],self.array[i]
                    t = i
            for i in range(t+1, a,-1):
                self.comparisonCount += 1
                if self.array[i] < self.array[i-1]:
                    self.forwardingCount += 1
                    self.array[i], self.array[i - 1] = self.array[i-1],self.array[i]
                    y = i
            b = t+1
            a = y-1

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)



