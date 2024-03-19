import random

# ПОСЛЕДОВАТЕЛЬНЫЙ ПОИСК
def sequentialSearch(array, target):
    count = 0
    for i, j in enumerate(array):
        count+=1
        if j == target:
            return count
    return count


# БИНАРНЫЙ ПОИСК
def binarySearch(array, target):
    l, r = 0, len(array) - 1
    count = 0
    while l < r:
        mid = (l + r) // 2
        count += 1
        if array[mid] == target:
            return count
        elif array[mid] > target:
            r = mid - 1
        elif array[mid] < target:
            l = mid + 1
    count += 1
    if array[l] == target:
        return count
    return count


# ПОИСК ФИБОНАЧЧИ С ПРОВЕРКОЙ
def FibNumLessThenSize(size):
    first = 0
    second = 1
    temp = first + second
    while temp < size + 1:
        first = second
        second = temp
        temp = first + second
    return [first, second, temp]


def fibSearch(array, target):
    count = 0
    fibNums = FibNumLessThenSize(len(array))
    m = fibNums[2] - 1 - len(array)
    i = fibNums[1] - m
    p = fibNums[0]
    q = fibNums[1] - fibNums[0]
    while p >= 1 and q >= 0:
        count += 1
        if i < 0:
            i = i + q
            p = p - q
            q = q - p
        elif i >= len(array):
            i = i - q
            temp = p
            p = q
            q = temp - q
        elif array[i] > target:
            i = i - q
            temp = p
            p = q
            q = temp - q
        elif array[i] < target:
            i = i + q
            p = p - q
            q = q - p
        elif array[i] == target:
            return count
    return count


# ПОИСК ФИБОНАЧЧИ БЕЗ ПРОВЕРКИ
def fibSearchAlt(array, target):
    count = 0
    fibNums = FibNumLessThenSize(len(array))
    if array[0] == target:
        return count
    m = fibNums[2] - 1 - len(array)
    i = fibNums[1]
    if target > array[i]:
        i = i - m
    p = fibNums[0]
    q = fibNums[1] - fibNums[0]
    while p >= 1 and q >= 0:
        count += 1
        if i >= len(array):
            i = i - q
            temp = p
            p = q
            q = temp - q
        elif array[i] == target:
            return count
        elif array[i] > target:
            i = i - q
            temp = p
            p = q
            q = temp - q
        elif array[i] < target:
            i = i + q
            p = p - q
            q = q - p

    return count


# БИНАРНОЕ ДЕРЕВО ПОИСКА
class Node:
    val = 0
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class tree:
    root = None

    def __init__(self, val):
        self.root = Node(val)

    def add(self, val):
        temp = self.root
        node = Node(val)
        while True:
            if temp.val > node.val:
                if temp.left is None:
                    temp.left = node
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    break
                else:
                    temp = temp.right

    def show(self, node):
        if node is None:
            return
        print(node, end=' ')
        self.show(node.left)
        self.show(node.right)

    def search(self, node, target, count):
        if node is None:
            return count
        count += 1
        if target == node.val:
            return count
        elif target > node.val:
            return self.search(node.right, target, count)
        elif target < node.val:
            return self.search(node.left, target, count)


# ЦИФРОВОЙ ПОИСК
class digNode:
    isEnd = False
    branch = [None, None, None, None, None, None, None, None, None, None]

    def __init__(self):
        self.isEnd = False
        self.branch = [None, None, None, None, None, None, None, None, None, None]


class digTree:
    root = digNode()

    def add(self, num: int):
        temp = self.root
        num = str(num)
        nums = [int(i) for i in num]
        for i in nums:
            if temp.branch[i] is not None:
                temp = temp.branch[i]
            else:
                temp.branch[i] = digNode()
                temp = temp.branch[i]
        temp.isEnd = True

    def search(self, target):
        count = 0
        temp = self.root
        num = str(target)
        nums = [int(i) for i in num]
        for i in nums:
            count += 1
            if temp.branch[i] is not None:
                temp = temp.branch[i]
            else:
                return count
        count += 1
        if temp.isEnd:
            return count
        else:
            return count


# ПОИСК В РБ ДЕРЕВЕ
BLACK = "B"
RED = 'R'
class RBNode:
    val = 0
    color = BLACK
    left = None
    right = None
    father = None

    def __init__(self, val, color=RED):
        self.val = val
        self.color = color


class RBTree:
    root = RBNode(None, BLACK)

    def __init__(self, val):
        self.root.val = val
        self.root.left = RBNode(None, BLACK)
        self.root.right = RBNode(None, BLACK)
        self.root.left.father = self.root
        self.root.right.father = self.root

    def rotate(self, node):
        p = node
        f = p.father
        if f is None:
            return 1
        if f.color == BLACK:
            return 1
        g = f.father
        fIsLeftSon = g.left == f
        u = g.right if fIsLeftSon else g.left
        if fIsLeftSon:
            if u.color == RED and f.color == RED:
                return self.rotate1Left(p,f,g,u)
            elif u.color == BLACK and f.right == p:
                return self.rotate2Left(p,f,g,u)
            elif u.color == BLACK and f.left == p:
                return self.rotate3Left(p,f,g,u)
        else:
            if u.color == RED and f.color == RED:
                return self.rotate1Right(p,f,g,u)
            elif u.color == BLACK and f.left == p:
                return self.rotate2Right(p,f,g,u)
            elif u.color == BLACK and f.right == p:
                return self.rotate3Right(p,f,g,u)

    def rotate1Left(self,p,f,g,u):
        f.color = BLACK
        u.color = BLACK
        g.color = RED
        return self.rotate(g)
    def rotate2Left(self,p,f,g,u):
        f.right = p.left
        f.right.father = f
        g.left = p
        p.father = g
        p.left = f
        f.father = p
        return self.rotate(f)

    def rotate3Left(self,p,f,g,u):
        if g.father is None:
            self.root = f
            f.father = None
        else:
            gIsLeftSon = g.father.left == g
            if gIsLeftSon:
                g.father.left = f
            else:
                g.father.right = f
            f.father = g.father
        g.left = f.right
        g.left.father = g
        f.right = g
        g.father = f
        f.color = BLACK
        g.color = RED
        return self.rotate(p)

    def rotate1Right(self,p,f,g,u):
        f.color = BLACK
        u.color = BLACK
        g.color = RED
        return self.rotate(g)

    def rotate2Right(self,p,f,g,u):
        g.right = p
        p.father = g
        f.left = p.right
        f.left.father = f
        p.right = f
        f.father = p
        return self.rotate(f)

    def rotate3Right(self,p,f,g,u):
        if g.father is None:
            self.root = f
            f.father = None
        else:
            gIsLeftSon = g.father.left == g
            if gIsLeftSon:
                g.father.left = f
            else:
                g.father.right = f
            f.father = g.father
        g.right = f.left
        g.right.father = g
        f.left = g
        g.father = f
        f.color = BLACK
        g.color = RED
        return self.rotate(p)

    def add(self, num):
        # print(num)
        node = RBNode(num)
        # print(node.val)
        node.left = RBNode(None, BLACK)
        node.left.father = node
        node.right = RBNode(None, BLACK)
        node.right.father = node
        temp = self.root
        isLeft = False
        while temp.val is not None:
            # print(temp.val)
            if num < temp.val:
                temp = temp.left
                isLeft = True
            else:
                temp = temp.right
                isLeft = False
        temp = temp.father
        if isLeft:
            temp.left = node
            node.father = temp
        else:
            temp.right = node
            node.father = temp
        self.rotate(node)
        self.root.color = BLACK

    def show(self, node):
        if node.val is None:
            return
        print(node.val,node.color, end=' ')
        self.show(node.left)
        self.show(node.right)

    def search(self, target):
        temp = self.root
        count = 0
        while temp.val is not None:

            if temp.val == target:
                count += 1
                return count
            elif temp.val > target:
                count += 1
                temp = temp.left
            else:
                count += 1
                temp = temp.right
        return count


def hashSearch(table, target):
    count = 0
    index = target % 1000
    for i in table[index]:
        count+=1
        if i==target:
            return count
    return count




# формирование массивов для поиска
array = list()
size = 200000
test_count = 100
for i in range(size):
    array.append(random.randint(0, 10000)*2)

# поиск с хэшированием
hashList = []
for i in range(1000):
    hashList.append([])
for i in array:
    index = i % 1000
    hashList[index].append(i)

binaryTree = tree(array[0])
rbTree = RBTree(array[0])
digT = digTree()
for i in range(1, size):
    binaryTree.add(array[i])
    rbTree.add(array[i])
    digT.add(array[i])
array.sort()


array_for_suc_search = list()
array_for_bad_search = list()
for i in range(test_count):
    array_for_suc_search.append(array[random.randint(0, size-1)])
    array_for_bad_search.append(random.randint(0,10000)*2+1)

#начальные определения для поиска
sequentialCount = 0
binaryCount = 0
fibCount = 0
fibAltCount = 0
binaryTreeCount = 0
rbTreeCount = 0
digCount = 0
hashCount = 0
count = 1
for i in array_for_suc_search:
    sequentialCount += (sequentialSearch(array, i))
    binaryCount += binarySearch(array, i)
    fibCount += fibSearch(array, i)
    fibAltCount += fibSearchAlt(array, i)
    binaryTreeCount += binaryTree.search(binaryTree.root, i , 0)
    rbTreeCount += rbTree.search(i)
    digCount += digT.search(i)
    hashCount += hashSearch(hashList, i)
sequentialCount = sequentialCount/test_count
binaryCount /= test_count
fibCount /= test_count
fibAltCount /= test_count
binaryTreeCount /= test_count
rbTreeCount /= test_count
digCount /= test_count
hashCount /= test_count
print("Успешный поиск")
print("последовательный поск: "+str(sequentialCount))
print("бинарный поиск: " + str(binaryCount))
print("поиск фибоначчи: " + str(fibCount))
print("альт поиск фибоначчи: " + str(fibAltCount))
print("дерево бинарного поиска: " + str(binaryTreeCount))
print("красно-черное дерево: " + str(rbTreeCount))
print("цифровое дерево: " + str(digCount))
print("хэш: " + str(hashCount))


sequentialCount = 0
binaryCount = 0
fibCount = 0
fibAltCount = 0
binaryTreeCount = 0
rbTreeCount = 0
digCount = 0
hashCount = 0
count = 1
for i in array_for_bad_search:
    sequentialCount += (sequentialSearch(array, i))
    binaryCount += binarySearch(array, i)
    fibCount += fibSearch(array, i)
    fibAltCount += fibSearchAlt(array, i)
    binaryTreeCount += binaryTree.search(binaryTree.root, i , 0)
    rbTreeCount += rbTree.search(i)
    digCount += digT.search(i)
    hashCount += hashSearch(hashList, i)
sequentialCount = sequentialCount/test_count
binaryCount /= test_count
fibCount /= test_count
fibAltCount /= test_count
binaryTreeCount /= test_count
rbTreeCount /= test_count
digCount /= test_count
hashCount /= test_count
print("Безуспешный поиск")
print("последовательный поск: "+str(sequentialCount))
print("бинарный поиск: " + str(binaryCount))
print("поиск фибоначчи: " + str(fibCount))
print("альт поиск фибоначчи: " + str(fibAltCount))
print("дерево бинарного поиска: " + str(binaryTreeCount))
print("красно-черное дерево: " + str(rbTreeCount))
print("цифровое дерево: " + str(digCount))
print("хэш: " + str(hashCount))












