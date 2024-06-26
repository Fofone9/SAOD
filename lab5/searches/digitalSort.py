import random


class digitalSort:
    def __init__(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 100000))
        self.forwardingCount = 0
        self.comparisonCount = 0

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 1000))

    def sort(self):
        temp = [[] for k in range(10)]
        n = len(str(max(self.array)))
        for i in range (n):
            for elem in self.array:
                digit = (elem//10**i)%10
                temp[digit].append((elem))
                self.forwardingCount += 1
                self.comparisonCount += 1
            self.array = []
            for row in temp:
                self.array.extend(row)
            temp = [[]for k in range(10)]

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()


