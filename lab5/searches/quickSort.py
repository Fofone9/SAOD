import random


class Node:
    def __init__(self, f, l):
        self.f = f
        self.l = l
        self.next = None

class stack:
    def __init__(self,f, l):
        self.root = Node(f,l)

    def push(self, f, l):
        node = Node(f,l)
        node.next = self.root
        self.root = node

    def pop(self):
        node = self.root
        self.root = self.root.next
        return node

    def clear(self):
        self.root = None


class quickSort:
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
            self.array.append(random.randint(0, 100000))
    def sort(self):
        S = stack(0,0)
        f = 0
        l = self.size-1
        while f < l:
            k = random.randint(f, l)
            self.array[f], self.array[k] = self.array[k], self.array[f]
            self.forwardingCount += 1

            i = f+1

            while i < self.size and self.array[i] < self.array[f]:
                self.comparisonCount += 1
                i = i + 1
            j = l
            while self.array[j] > self.array[f]:
                self.comparisonCount += 1
                j = j - 1
            while i < j:
                self.comparisonCount += 1
                self.forwardingCount += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1
                while self.array[i] < self.array[f]:
                    self.comparisonCount += 1
                    i += 1
                j -= 1
                while self.array[j] > self.array[f]:
                    self.comparisonCount += 1
                    j -= 1
            self.forwardingCount += 1
            self.array[f], self.array[j] = self.array[j], self.array[f]
            self.comparisonCount += 1
            if j-1 <= f and l <= j+1:
                node = S.pop()
                f = node.f
                l = node.l
            elif j-1 <= f and l >= j+1:
                f = j+1
            elif j-1 > f and l <= j+1:
                l = j-1
            elif j-1 > f and l >= j+1:
                if j-f > l-j:
                    S.push(f, j-1)
                    f = j+1
                else:
                    S.push(j+1, l)
                    l = j-1
        S.clear()

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()

