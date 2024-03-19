# БИНАРНОЕ ДЕРЕВО ПОИСКА
class Node:
    val = None
    left = None
    right = None
    father = None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class binariTree:
    root = None
    deleteCount = 0
    def __init__(self, val):
        self.root = Node(val)
        self.root.left = Node(None)
        self.root.right = Node(None)
        self.root.left.father = self.root
        self.root.right.father = self.root

    def add(self, val):
        temp = self.root
        while(temp.val is not None):
            if temp.val > val:
                temp = temp.left
            else:
                temp = temp.right
        temp.val = val
        temp.left = Node(None)
        temp.right = Node(None)
        temp.left.father = temp
        temp.right.father = temp

    def delete(self, node):
        # у узла нет детей
        if node.left.val is None and node.right.val is None:
            node.left = None
            node.right = None
            node.val = None
            self.deleteCount = 1
        # если есть левый сын
        elif node.left.val is not None and node.right.val is None:
            node.val = node.left.val
            node.right = node.left.right
            node.left = node.left.left
            self.deleteCount = 1
        # если есть првый сын
        elif node.left.val is None and node.right.val is not None:
            node.val = node.right.val
            node.left = node.right.left
            node.right = node.right.right
            self.deleteCount = 1
        # если есть оба сына
        else:
            temp = node.right
            while temp.left.val is not None:
                temp = temp.left
            node.val = temp.val
            self.delete(temp)
            self.deleteCount = 2

    def searchNode(self, val):
        temp = self.root
        while temp.val is not None:
            if temp.val == val:
                return temp
            elif temp.val > val:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def show(self, node):
        if node.val is None:
            return
        print(node.val)
        self.show(node.left)
        self.show(node.right)


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
    count = 0

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
            return
        if f.color == BLACK:
            return
        g = f.father
        fIsLeftSon = g.left == f
        u = g.right if fIsLeftSon else g.left
        if fIsLeftSon:
            if u.color == RED and f.color == RED:
                return self.rotate1Left(p, f, g, u)
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
        self.count += 1
        return self.rotate(g)

    def rotate2Left(self,p,f,g,u):
        f.right = p.left
        f.right.father = f
        g.left = p
        p.father = g
        p.left = f
        f.father = p
        self.count += 1
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
        self.count += 1
        return

    def rotate1Right(self,p,f,g,u):
        f.color = BLACK
        u.color = BLACK
        g.color = RED
        self.count += 1
        return self.rotate(g)

    def rotate2Right(self,p,f,g,u):
        g.right = p
        p.father = g
        f.left = p.right
        f.left.father = f
        p.right = f
        f.father = p
        self.count += 1
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
        self.count += 1
        return

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
        temp = self.count
        self.count = 0
        return temp

    def deleteNode(self, node):
        if node.left.val is not None and node.right.val is not None:
            return 0
        # тут не надо дополнительных коррекций так как черная высота не меняется
        if node.color == RED:
            if node.father.left == node: #если узел является левым сыном
                if node.left.val is None:
                    node.father.left = node.right
                    node.right.father = node.father

                else:
                    node.father.left = node.left
                    node.left.father = node.father

            else:
                if node.left.val is None:
                    node.father.right = node.right
                    node.right.father = node.father

                else:
                    node.father.right = node.left
                    node.left.father = node.father

        else:
            if node.father.left == node:
                if node.left.val is None:
                    node.father.left = node.right
                    node.right.father = node.father
                    self.correction(node.right)
                else:
                    node.father.left = node.left
                    node.left.father = node.father
                    self.correction(node.left)
            else:
                if node.left.val is None:
                    node.father.right = node.right
                    node.right.father = node.father
                    self.correction(node.right)
                else:
                    node.father.right = node.left
                    node.left.father = node.father
                    self.correction(node.right)
        temp = self.count
        self.count = 0
        return temp

    # коррекции при удалении: цифры - случаи
    def correction(self, node):
        p = node
        f = node.father
        isLeft = p == f.left
        if isLeft:
            w = f.right
        else:
            w = f.left
        if p.color == RED:
            p.color = BLACK
            return
        if w.val is None:
            return
        if isLeft:
            if w.color == RED:
                return self.correction1Left(p, w, f)
            elif w.right.color == BLACK and w.left.color == BLACK:
                return self.correction2Left(p, w, f)
            elif w.right.color == BLACK and w.left.color == RED:
                return self.correction3Left(p, w, f)
            elif w.right.color == RED:
                return self.correction4Left(p, w, f)
        else:
            if w.color == RED:
                return self.correction1Right(p, w, f)
            elif w.right.color == BLACK and w.left.color == BLACK:
                return self.correction2Right(p, w, f)
            elif w.right.color == RED and w.left.color == BLACK:
                return self.correction3Right(p, w, f)
            elif w.left.color == RED:
                return self.correction4Right(p, w, f)

    def correction1Left(self, p, w, f):
        fatherIsLeft = False
        if f.father.left == f:
            fatherIsLeft = True
        if fatherIsLeft:
            f.father.left = w
        else:
            f.father.right = w
        w.father = f.father
        f.right = w.left
        f.right.father = f
        w.left = f
        f.father = w
        f.color = RED
        w.color = BLACK
        self.count += 1
        return self.correction(p)

    def correction2Left(self, p, w, f):
        w.color = RED
        return self.correction(f)

    def correction3Left(self, p, w, f):
        c = w.left
        f.right = c
        c.father = f
        w.left = c.right
        w.left.father = w
        c.right = w
        w.father = c
        c.color = BLACK
        w.color = RED
        self.count += 1
        return self.correction(p)

    def correction4Left(self, p, w, f):
        fatherIsLeft = False
        if f.father.left == f:
            fatherIsLeft = True
        if fatherIsLeft:
            f.father.left = w
        else:
            f.father.right = w
        w.father = f.father
        f.right = w.left
        f.right.father = f
        w.left = f
        f.father = w
        w.color = f.color
        w.right.color = BLACK
        f.color = BLACK
        self.count += 1
        return

    def correction1Right(self, p, w, f):
        fatherIsLeft = f.father.left == f
        if fatherIsLeft:
            f.father.left = w
        else:
            f.father.right = w
        w.father = f.father
        e = w.right
        w.right = f
        f.father = w
        f.left = e
        e.father = f
        w.color = BLACK
        f.color = RED
        self.count += 1
        return self.correction(p)

    def correction2Right(self, p, w, f):
        w.color = RED
        return self.correction(f)

    def correction3Right(self, p, w, f):
        e = w.right
        e.father = f
        f.left = e
        w.right = e.left
        w.right.father = w
        e.left = w
        w.father = e
        e.color = BLACK
        w.color = RED
        self.count += 1
        return self.correction(p)

    def correction4Right(self, p, w, f):
        fatherIsLeft = False
        if f.father.left == f:
            fatherIsLeft = True
        if fatherIsLeft:
            f.father.left = w
        else:
            f.father.right = w
        w.father = f.father
        e = w.right
        w.right = f
        f.father = w
        f.left = e
        e.father = f
        w.color = f.color
        f.color = BLACK
        w.left.color = BLACK
        self.count += 1
        return

    def show(self, node):
        if node.val is None:
            return
        print(node.val,node.color, end=' ')
        self.show(node.left)
        self.show(node.right)

    def search(self, target):
        temp = self.root
        while temp.val is not None:
            if temp.val == target:
                return temp
            elif temp.val > target:
                temp = temp.left
            else:
                temp = temp.right
        return None


# Тесты
import random
array = list()
size = 10000
search_size = 10000
for i in range(size):
    array.append(random.randint(0, 10000))
someTree = RBTree(random.randint(0, 10000))
biTree = binariTree(someTree.root.val)
for i in array:
    someTree.add(i)
    biTree.add(i)

search_array = list()
bi_delete_count = 0
bi_add_count = 0
rb_delete_count = 0
rb_add_count = 0
count = 0
for i in range(search_size):
    search_array.append(random.randint(0, 10000))
for i in search_array:
    isFind = someTree.search(i)
    if isFind is None:
        rb_add_count += someTree.add(i)
    else:
        rb_delete_count += someTree.deleteNode(isFind)

for i in search_array:
    node = biTree.searchNode(i)
    if node is None:
        bi_add_count += 1
        biTree.add(i)
    else:
        biTree.delete(node)
        bi_delete_count += biTree.deleteCount
        biTree.deleteCount = 0

print('Количество сравнений' + str(search_size))
print("Бинарное дерево:")
print("Вращений при удалении:" + str(bi_delete_count))
print("Вращений при добавлении:" + str(bi_add_count))
print("Красно-черное дерево:")
print("Вращений при удалении:" + str(rb_delete_count))
print("Вращений при добавлении:" + str(rb_add_count))

