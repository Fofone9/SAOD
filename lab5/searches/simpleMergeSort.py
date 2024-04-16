import random


class simpleMergeSort:
    def __init__(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 10))
        self.forwardingCount = 0
        self.comparisonCount = 0

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 10))

    def merge(self, array):
        if len(array) == 1:
            return array
        leftArray = self.merge(array[0:len(array)//2])
        rightArray = self.merge(array[len(array)//2:len(array)])
        result = list()
        i = 0
        j = 0

        while i < len(leftArray) and j < len(rightArray):
            self.comparisonCount += 1
            if leftArray[i] < rightArray[j]:
                self.forwardingCount += 1
                result.append(leftArray[i])
                i += 1
            else:
                self.forwardingCount += 1
                result.append(rightArray[j])
                j += 1
        while i < len(leftArray):
            self.forwardingCount += 1
            result.append(leftArray[i])
            i += 1
        while j < len(rightArray):
            self.forwardingCount += 1
            result.append(rightArray[j])
            j += 1
        return result

    def sort(self):
        self.array = self.merge(self.array)

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)


