import random


class piramidSort:
    def __init__(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 100000))
        self.forwardingCount = 0
        self.comparisonCount = 0

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 10))

    def sort(self):
        for j in range((len(self.array)-2)//2, -1, -1):
            self.siftDown(j, len(self.array))

        for end in range(len(self.array)-1, 0, -1):
            self.swap(0, end)
            self.siftDown(0, end)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        self.forwardingCount += 1

    def siftDown(self, i, upper):
        while (True):
            l, r = i*2+1, i*2+2
            self.comparisonCount += 1
            if max(l, r) < upper:
                self.comparisonCount += 1
                if self.array[i] >= max(self.array[l], self.array[r]):
                    break
                elif self.array[l] > self.array[r]:
                    self.swap(i, l)
                    i = l
                else:
                    self.swap(i, r)
                    i = r
            elif l < upper:
                self.comparisonCount += 1
                if self.array[l] > self.array[i]:
                    self.swap(i, l)
                    i = l
                else:
                    break
            elif r < upper:
                self.comparisonCount += 1
                if self.array[r] > self.array[i]:
                    self.swap(i, r)
                    i = r
                else:
                    break
            else:
                break

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)



