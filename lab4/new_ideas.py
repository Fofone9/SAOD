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

    def show(self, node = root):
        if node.val is None:
            return
        print(node.val)
        self.show(node.left)
        self.show(node.right)


array = [4, 2, 6, 12, 334, 2, 121, 22, 11, 34, 21]
searchArray = [12, 2, 1, 5, 11]
tree = binariTree(13)
for i in array:
    tree.add(i)
delCount = 0
addCount = 0
for i in searchArray:
    node = tree.searchNode(i)
    if node is None:
        addCount+=1
        tree.add(i)
    else:
        tree.delete(node)
        delCount += tree.deleteCount
        tree.deleteCount = 0
print(delCount)
print(addCount)