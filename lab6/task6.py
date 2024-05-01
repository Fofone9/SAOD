import math
class Node:
    def __init__(self, val):
        self.val = val
        self.edge = dict()
        self.label = math.inf
        self.way = list()


class Edge:
    def __init__(self, weight, node):
        self.weight = weight
        self.adjasentNode = node


class Graf:
    def __init__(self):
        self.nodes = dict()

    def addNode(self, val):
        node = Node(val)
        self.nodes[val] = node

    def addEdge(self, start, end, weight):
        if start not in self.nodes.keys():
            self.nodes[start] = Node(start)
        if end not in self.nodes.keys():
            self.nodes[end] = Node(end)
        if weight > 0:
            edge = Edge(weight, self.nodes[end])
            self.nodes[start].edge[end] = edge

    def shortestWayFrom(self, name):
        node = self.nodes[name]
        node.label = 0
        last = node
        T = list(self.nodes.values())
        T.remove(node)
        while len(T) != 0:
            for v in T:
                w = math.inf
                if v.val in last.edge.keys():
                    w = last.edge[v.val].weight
                if v.label > last.label + w:
                    v.label = last.label + w
                    v.way = last.way.copy()
                    v.way.append(last.val)
            minimal = T[0]
            for i in T:
                if i.label < minimal.label:
                    minimal = i
            T.remove(minimal)
            last = minimal

    def showWays(self):
        self.nodes = dict(sorted(self.nodes.items()))
        for i in self.nodes.values():
            i.way.append(i.val)
            print(i.val, i.way, i.label)


g = Graf()
g.addEdge('a','b', 8)
g.addEdge('a','e', 10)
g.addEdge('a','f', 1)
g.addEdge('c','b', 2)
g.addEdge('c','d', 6)
g.addEdge('c','g', 3)
g.addEdge('d','e', 1)
g.addEdge('f','b', 5)
g.addEdge('f','c', 2)
g.addEdge('f','g', 7)
g.addEdge('g','d', 2)

g.shortestWayFrom('a')
g.showWays()


