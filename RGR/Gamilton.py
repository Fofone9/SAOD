import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, val):
        self.val = val
        self.edge = dict()


class Edge:
    def __init__(self, node):
        self.adjasentNode = node


class Graf:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()
        self.visited = list()
        self.start = None
        self.way = list()
        self.size = 0

    def addNode(self, val):
        node = Node(val)
        self.nodes[val] = node
        self.edges[val] = list()
        self.size += 1

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

    def createHamiltonCycle(self):
        current = list()
        for key in self.nodes.keys():
            current.append(self.nodes[key])
            self.start = self.nodes[key]
            while len(current) != 0:
                node = current.pop()
                self.visited.append(node.val)
                current = self.visite(current, node)
                if len(self.way) != 0:
                    return
        print("NETU")

    def visite(self, visited, node):
        edges = self.edges[node.val]
        nextVisites = list()
        hasStartNode = False
        for edge in edges:
            if edge.adjasentNode.val not in self.visited:
                nextVisites.append(edge.adjasentNode)
            if edge.adjasentNode == self.start:
                hasStartNode = True
        if len(nextVisites) == 0 and hasStartNode:
            self.way = self.visited.copy()
            self.way.append(self.start.val)
            print(self.way)
        elif len(nextVisites) == 0:
            self.visited.pop
        visited += nextVisites
        return visited

    def show(self):
        G = nx.Graph()
        for i in self.nodes.keys():
            G.add_node(i)
        for i in self.edges.keys():
            for j in self.edges[i]:
                G.add_edge(i, j.adjasentNode.val)
        nx.draw(G, with_labels = True);
        plt.show()

g = Graf()
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(1, 6)
g.addEdge(6, 1)
g.addEdge(2, 7)
g.addEdge(3, 4)
g.addEdge(3, 8)
g.addEdge(4, 5)
g.addEdge(4, 9)
g.addEdge(5, 1)
g.addEdge(5, 10)
g.addEdge(2, 1)
g.addEdge(3, 2)
g.addEdge(7, 2)
g.addEdge(4, 3)
g.addEdge(8, 3)
g.addEdge(5, 4)
g.addEdge(9, 4)
g.addEdge(10, 5)
g.addEdge(6, 11)
g.addEdge(11, 6)
g.addEdge(11, 10)
g.addEdge(10, 11)
g.addEdge(10, 15)
g.addEdge(15, 10)
g.addEdge(15, 9)
g.addEdge(9, 15)
g.addEdge(9, 14)
g.addEdge(14, 9)
g.addEdge(14, 8)
g.addEdge(8, 14)
g.addEdge(8, 13)
g.addEdge(13, 8)
g.addEdge(13, 7)
g.addEdge(7, 13)
g.addEdge(7, 12)
g.addEdge(12, 7)
g.addEdge(12, 6)
g.addEdge(6, 12)
g.addEdge(12, 17)
g.addEdge(17, 12)
g.addEdge(11, 16)
g.addEdge(16, 11)
g.addEdge(15, 20)
g.addEdge(20, 15)
g.addEdge(14, 19)
g.addEdge(19, 14)
g.addEdge(13, 18)
g.addEdge(18, 13)
g.addEdge(16, 17)
g.addEdge(17, 16)
g.addEdge(17, 18)
g.addEdge(18, 17)
g.addEdge(18, 19)
g.addEdge(19, 18)
g.addEdge(19, 20)
g.addEdge(20, 19)
g.addEdge(20, 16)
g.addEdge(16, 20)
g.show()
g.createHamiltonCycle()

