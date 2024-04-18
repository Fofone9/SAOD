import random


class bubbleSort:
    def __init__(self, size):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.array = list()
        self.size = size
        for i in range(size):
            self.array.append(random.randint(0, 100000))

    def setArray(self, size):
        self.array = list()
        self.size = size
        for i in range(size):
            self.array.append(random.randint(0, 10))

    def sort(self):
        a = 0
        b = self.size
        while b != 1:
            t = 0
            y = self.size
            for i in range(a, b-1):
                self.comparisonCount += 1
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i + 1] = self.array[i+1],self.array[i]
                    self.forwardingCount += 1

                    t = i
            b = t+1

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()




