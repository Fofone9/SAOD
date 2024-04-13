import random


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.past = None


class simpleMergeSort:
    def __init__(self):
        self.root = Node(random.randint(0, 10))
        self.size = 0

    def setList(self, size):
        self.size = size
        temp = self.root
        for i in range(size-1):
            node = Node(random.randint(0, 10))
            node.past = temp
            temp.next = node
            temp = temp.next

    def merge(self, l, r):
        if r - l == 0:
            return
        m = (r - l)//2
        self.merge(l, m)
        self.merge(m+1, r)
        leftNode = self.root
        for i in range(l):
            leftNode = leftNode.next
        rightNode = self.root
        for i in range(m):
            rightNode = rightNode.next
        i = l
        j = m+1
        while i<m+1 and j<r:
            pass

    def sort(self):
        pass

    def show(self):
        for i in self.array:
            print(i, end=' ')
        print()


test = simpleMergeSort()
test.setArray(10)
test.show()
test.sort()
test.show()