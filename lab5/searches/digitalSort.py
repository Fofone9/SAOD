import random


class digitalSort:
    def __init__(self):
        self.array = list()

    def setArray(self, size):
        self.array = list()
        for i in range(size):
            self.array.append(random.randint(0, 10))

    def sort(self):
        pass