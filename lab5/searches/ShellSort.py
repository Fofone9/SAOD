import random


class ShellSort:
    def __init__(self):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.array = list()
        self.h = list()

    def setArray(self, size):
        self.array = list()
        self.h = list()
        for i in range(size):
            self.array.append(random.randint(0, 10))
        i = 1
        while i < size:
            self.h.append(i)
            i = i*2
        self.h.sort(reverse=True)

    def sort(self):
        for h in self.h:
            for j in range(h, len(self.array)):
                i = j-h
                key = self.array[j]
                while i >= 0 and key < self.array[i]:
                    self.comparisonCount += 1
                    self.forwardingCount += 1
                    self.array[i+h] = self.array[i]
                    i = i - h
                self.array[i+h] = key
                self.forwardingCount += 1

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)

