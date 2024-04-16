import random

class Node:
    def __init__(self, val):
        self.next = None
        self.past = None

        self.val = val


class InsertionSortIntoLinkedList:
    def __init__(self, size):
        self.forwardingCount = 0
        self.comparisonCount = 0
        self.size = 0
        self.array = Node(random.randint(0, 10))
        self.size = size
        temp = self.array
        for i in range(size - 1):
            temp.next = Node(random.randint(0, 10))
            temp.next.past = temp
            temp = temp.next

    def setArray(self, size):
        self.array = Node(random.randint(0, 10))
        self.size = size
        temp = self.array
        for i in range(size-1):
            temp.next = Node(random.randint(0, 10))
            temp.next.past = temp
            temp = temp.next

    def sort(self):
        temp = self.array.next
        while temp is not None:
            key = temp.past
            next = temp.next
            while key is not None and key.val > temp.val:
                key = key.past
                self.comparisonCount += 1
            temp.past.next = temp.next
            if temp.next is not None:
                self.forwardingCount += 1
                temp.next.past = temp.past
            if key is None:
                self.array.past = temp
                temp.next = self.array
                temp.past = None
                self.array = temp
                self.forwardingCount += 2
            else:
                thisNext = key.next
                key.next = temp
                temp.past = key
                if thisNext is not None:
                    thisNext.past = temp
                temp.next = thisNext
                self.forwardingCount += 2
            temp = next

    def show(self):
        temp = self.array
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next
        print()
        print('Колическтво пересылок:', self.forwardingCount)
        print('Количество сравнений', self.comparisonCount)



