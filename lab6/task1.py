class Node:
    def __init__(self, val):
        self.val = val
        self.edge = dict()


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
        edge = Edge(weight, self.nodes[end])
        self.nodes[start].edge[end] = edge

    def show(self):
        for i in self.nodes.keys():
            node = self.nodes[i]
            for j in node.edge.keys():
                edge = node.edge[j]
                print(node.val, '-', edge.weight, '-', edge.adjasentNode.val)




data = [[7,5,1],[7,6,1],[6,4,1],[8,-1,1],[5,9,1]]
graf = Graf()
for i in data:
    graf.addEdge(i[0],i[1],i[2])
graf.show()
