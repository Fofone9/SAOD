import networkx as nx
import matplotlib.pyplot as plt
class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.root = None
        self.listing = list()

    def push(self, val):
        node = StackNode(val)
        node.next = self.root
        self.root = node
        self.listing.insert(0, val)

    def pop(self):
        node = self.root
        self.root = self.root.next
        self.listing.pop(0)
        return node.val

    def isEmpty(self):
        return self.root is None

    def empty(self):
        self.listing = list()
        while self.root != None:
            self.root = self.root.next


class Node:
    def __init__(self, val):
        self.val = val
        self.num = 0
        self.edge = dict()


class Edge:
    def __init__(self, node):
        self.adjasentNode = node


class Graf:
    def __init__(self):
        self.nodes = dict()
        self.S = Stack()
        self.i = 0
        self.j = 0
        self.C = list()
        self.edges = dict()
        self.size = 0

    def addNode(self, val):
        node = Node(val)
        self.nodes[val] = node

    def addEdge(self, start, end):
        if start not in self.nodes.keys():
            self.nodes[start] = Node(start)
            self.edges[start] = list()
            self.size += 1
        if end not in self.nodes.keys():
            self.nodes[end] = Node(end)
            self.edges[end] = list()
            self.size += 1
        edge = Edge(self.nodes[end])
        self.edges[start].append(edge)
        self.nodes[start].edge[end] = edge

    def task(self):
        self.S = Stack()
        self.i = 0
        self.j = 0
        self.C = list()
        for x in self.nodes.values():
            x.num = 0
        for x in self.nodes.values():
            self.S.empty()
            if x.num == 0:
                self.cycle(x, None)

    def cycle(self, v, u):
        self.i += 1
        v.num = self.i
        self.S.push(v)
        for edge in v.edge.values():
            w = edge.adjasentNode
            if w.num == 0:
                self.cycle(w, v)
                self.S.pop()
            elif w.num < v.num and w != u:
                self.j += 1
                C = list()
                C.append(w.val)
                for i in self.S.listing:
                    C.append(i.val)
                    if i.val == w.val:
                        break
                self.C.append(C)

    def showTask(self):
        for i in self.C:
            print(i)
            g = nx.Graph()
            for node in i:
                g.add_node(node)
            for j in range (1,len(i)):
                g.add_edge(i[j-1], i[j])
            nx.draw(g, with_labels=True);
            plt.show()


    def show(self):
        for i in self.nodes.keys():
            node = self.nodes[i]
            for j in node.edge.keys():
                edge = node.edge[j]
                print(node.val, '-', edge.adjasentNode.val)
        G = nx.Graph()
        for i in self.nodes.keys():
            G.add_node(i)
        for i in self.edges.keys():
            for j in self.edges[i]:
                G.add_edge(i, j.adjasentNode.val)
        nx.draw(G, with_labels=True);
        plt.show()


graf = Graf()
data = {'a': ['b', 'e', 'f'],
        'b': ['a', 'c', 'f'],
        'c': ['b', 'd', 'f', 'g'],
        'd': ['c', 'e', 'g'],
        'e': ['a', 'd'],
        'f': ['a', 'b', 'c', 'g'],
        'g': ['c', 'd', 'f']}
for key in data.keys():
    for elem in data[key]:
        graf.addEdge(key, elem)
graf.task()
graf.showTask()
graf.show()
