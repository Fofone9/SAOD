import networkx as nx
import matplotlib.pyplot as plt
import time

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
        self.start = None
        self.path = list()
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
        for key in self.nodes.keys():
            current = [self.nodes[key]]
            start = current[0]
            visited = list()
            while len(current) != 0:
                node = current.pop()
                if node not in visited:
                    visited.append(node)
                # else:
                #     visited.pop()
                #     continue
                edges = node.edge
                if len(visited) == self.size and start.val in edges.keys():
                    listing = [item.val for item in visited]
                    listing.append(start.val)
                    self.path.append(listing)
                nextNodesForAddToCurrent = list()
                for edge in edges.values():
                    nextNode = edge.adjasentNode
                    if nextNode not in visited:
                        nextNodesForAddToCurrent.append(nextNode)
                current += nextNodesForAddToCurrent
                if len(nextNodesForAddToCurrent) == 0:
                    visited.pop()
                    while True:
                        temp = visited[-1]
                        nextNodes = list()
                        edges = temp.edge
                        for edge in edges.values():
                            nextNode = edge.adjasentNode
                            if nextNode not in visited:
                                nextNodes.append(nextNode)
                        if len(nextNodes) == 1:
                            visited.pop()
                        else:
                            break
    def showPath(self):
        for path in self.path:
            print('-'.join([str(item) for item in path]))
    def show(self):
        G = nx.Graph()
        for i in self.nodes.keys():
            G.add_node(i)
        for i in self.edges.keys():
            for j in self.edges[i]:
                G.add_edge(i, j.adjasentNode.val)

        nx.draw(G, with_labels=True)
        plt.show()


g = Graf()
# g.addEdge(1, 2)
# g.addEdge(1, 5)
# g.addEdge(2, 3)
# g.addEdge(1, 6)
# g.addEdge(6, 1)
# g.addEdge(2, 7)
# g.addEdge(3, 4)
# g.addEdge(3, 8)
# g.addEdge(4, 5)
# g.addEdge(4, 9)
# g.addEdge(5, 1)
# g.addEdge(5, 10)
# g.addEdge(2, 1)
# g.addEdge(3, 2)
# g.addEdge(7, 2)
# g.addEdge(4, 3)
# g.addEdge(8, 3)
# g.addEdge(5, 4)
# g.addEdge(9, 4)
# g.addEdge(10, 5)
# g.addEdge(6, 11)
# g.addEdge(11, 6)
# g.addEdge(11, 10)
# g.addEdge(10, 11)
# g.addEdge(10, 15)
# g.addEdge(15, 10)
# g.addEdge(15, 9)
# g.addEdge(9, 15)
# g.addEdge(9, 14)
# g.addEdge(14, 9)
# g.addEdge(14, 8)
# g.addEdge(8, 14)
# g.addEdge(8, 13)
# g.addEdge(13, 8)
# g.addEdge(13, 7)
# g.addEdge(7, 13)
# g.addEdge(7, 12)
# g.addEdge(12, 7)
# g.addEdge(12, 6)
# g.addEdge(6, 12)
# g.addEdge(12, 17)
# g.addEdge(17, 12)
# g.addEdge(11, 16)
# g.addEdge(16, 11)
# g.addEdge(15, 20)
# g.addEdge(20, 15)
# g.addEdge(14, 19)
# g.addEdge(19, 14)
# g.addEdge(13, 18)
# g.addEdge(18, 13)
# g.addEdge(16, 17)
# g.addEdge(17, 16)
# g.addEdge(17, 18)
# g.addEdge(18, 17)
# g.addEdge(18, 19)
# g.addEdge(19, 18)
# g.addEdge(19, 20)
# g.addEdge(20, 19)
# g.addEdge(20, 16)
# g.addEdge(16, 20)

# нет цикла
# g.addEdge(1,2)
# g.addEdge(2,1)
# g.addEdge(2,4)
# g.addEdge(4,2)
# g.addEdge(4,3)
# g.addEdge(3,4)
# g.addEdge(4,5)
# g.addEdge(5,4)
# g.addEdge(5,2)
# g.addEdge(2,5)
# g.addEdge(5,1)
# g.addEdge(1,5)

# g.addEdge(1,2)
# g.addEdge(2,1)
# g.addEdge(2,3)
# g.addEdge(3,2)
# g.addEdge(1,3)
# g.addEdge(3,1)
# 16 вершин 14 грани
g.addEdge(1,2)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(4,3)
g.addEdge(5,6)
g.addEdge(6,5)
g.addEdge(6,7)
g.addEdge(7,6)
g.addEdge(7,8)
g.addEdge(8,7)
g.addEdge(9,10)
g.addEdge(10,9)
g.addEdge(10,11)
g.addEdge(11,10)
g.addEdge(11,12)
g.addEdge(12,11)
g.addEdge(13,14)
g.addEdge(14,13)
g.addEdge(14,15)
g.addEdge(15,14)
g.addEdge(15,16)
g.addEdge(16,15)
g.addEdge(1,5)
g.addEdge(5,1)
g.addEdge(5,9)
g.addEdge(9,5)
g.addEdge(9,13)
g.addEdge(13,9)
g.addEdge(2,6)
g.addEdge(6,2)
g.addEdge(6,10)
g.addEdge(10,6)
g.addEdge(10,14)
g.addEdge(14,10)
g.addEdge(3,7)
g.addEdge(7,3)
g.addEdge(7,11)
g.addEdge(11,7)
g.addEdge(11,15)
g.addEdge(15,11)
g.addEdge(4,8)
g.addEdge(8,4)
g.addEdge(8,12)
g.addEdge(12,8)
g.addEdge(12,16)
g.addEdge(16,12)
start_time = time.time()
g.createHamiltonCycle()
end_time = time.time()
execution_time = end_time - start_time
print(execution_time*1_000)
g.show()
g.showPath()
