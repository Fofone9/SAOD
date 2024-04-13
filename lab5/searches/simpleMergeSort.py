import random


class simpleMergeSort:
    def __init__(self):
        self.array = list()

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
            if leftArray[i] < rightArray[j]:
                result.append(leftArray[i])
                i += 1
            else:
                result.append(rightArray[j])
                j += 1
        while i < len(leftArray):
            result.append(leftArray[i])
            i += 1
        while j < len(rightArray):
            result.append(rightArray[j])
            j += 1
        return result

    def sort(self):
        self.array = self.merge(self.array)

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()


test = simpleMergeSort()
test.setArray(10)
test.show()
test.sort()
test.show()