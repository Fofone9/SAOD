import random


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class simpleMergeSortForList:
    def __init__(self, size):
        self.root = Node(random.randint(0, 100000))
        self.size = size
        temp = self.root
        for i in range(size - 1):
            node = Node(random.randint(0, 100000))
            temp.next = node
            temp = temp.next
        self.forwardingCount = 0
        self.comparisonCount = 0

    def setList(self, size):
        self.size = size
        temp = self.root
        for i in range(size-1):
            node = Node(random.randint(0, 10))
            temp.next = node
            temp = temp.next

    def merge(self, l, r):
        left = self.root
        for i in range(l):
            left = left.next
        if r <= l:
            return left
        right = self.root
        # for i in range(r):
        #     right = right.next
        mid = (r+l)//2
        leftRoot = self.merge(l, mid)
        rightRoot = self.merge(mid+1, r)
        resultRoot = None
        i = l
        j = mid+1
        result = None
        self.comparisonCount += 1
        if leftRoot.val < rightRoot.val:
            self.forwardingCount += 1
            result = Node(leftRoot.val)
            i += 1
            leftRoot = leftRoot.next
        else:
            self.forwardingCount += 1
            result = Node(rightRoot.val)
            j += 1
            rightRoot = rightRoot.next
        resultRoot = result
        while i <= mid and j <= r:
            self.comparisonCount += 1
            if leftRoot.val < rightRoot.val:
                self.forwardingCount += 1
                result.next = Node(leftRoot.val)
                i += 1
                result = result.next
                leftRoot = leftRoot.next
            else:
                self.forwardingCount += 1
                result.next = Node(rightRoot.val)
                j += 1
                result = result.next
                rightRoot = rightRoot.next
        while i <= mid:
            self.forwardingCount += 1
            result.next = Node(leftRoot.val)
            i += 1
            result = result.next
            leftRoot = leftRoot.next
        while j <= r:
            self.forwardingCount += 1
            result.next = Node(rightRoot.val)
            j += 1
            result = result.next
            rightRoot = rightRoot.next
        return resultRoot



    def sort(self):
        self.root = self.merge(0, self.size-1)

    def show(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)


