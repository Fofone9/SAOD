
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
        if weight > 0:
            edge = Edge(weight, self.nodes[end])
            self.nodes[start].edge[end] = edge

    def ostTreeLenKrasal(self):
        edges = dict()
        groups = list()
        answer = 0
        # создание списка ребер
        for i in self.nodes.keys():
            node = self.nodes[i]
            groups.append([node.val])
            for j in node.edge.keys():
                weight = node.edge[j].weight
                if weight not in edges.keys():
                    edges[weight] = list()
                edges[weight].append((node.val, j))
        edges = dict(sorted(edges.items()))
        for i in edges.keys():
            print(i, edges[i])
        print(groups)
        for weight in edges.keys():
            for edge in edges[weight]:
                addingGr = list()
                for gr in groups:
                    if edge[1] in gr and edge[0] not in gr:
                        addingGr = gr
                        groups.remove(gr)
                        break
                for gr in groups:
                    if edge[0] in gr and edge[1] not in gr:
                        # gr += list(edge)
                        gr += addingGr
                        answer += weight
                        break
        print(answer)

    def ostTreeLenPrima(self):
        visited = list()
        unvisited = [i for i in self.nodes.keys()]
        answer = 0
        visited.append(unvisited.pop(0))
        while len(unvisited) != 0:
            minEdgeWeight = 100000
            minEdgeAim = 0
            for i in visited:
                node = self.nodes[i]
                edgeList = node.edge
                for point in edgeList.keys():
                    weight = edgeList[point].weight
                    if weight < minEdgeWeight and point not in visited:
                        minEdgeAim = point
                        minEdgeWeight = weight
            visited.append(minEdgeAim)
            unvisited.remove(minEdgeAim)
            answer += minEdgeWeight
        print(answer)

    def show(self):
        for i in self.nodes.keys():
            node = self.nodes[i]
            for j in node.edge.keys():
                edge = node.edge[j]
                print(node.val, '- (', edge.weight, ') -', edge.adjasentNode.val)


data = [[0,2,6,8,-1,-1,3,-1,-1],
        [2,0,9,3,-1,4,9,-1,-1],
        [6,9,0,7,-1,-1,-1,-1,-1],
        [8,3,7,0,5,5,-1,-1,-1],
        [-1,-1,-1,5,0,-1,8,9,-1],
        [-1,4,-1,5,-1,0,-1,6,4],
        [3,9,-1,-1,8,-1,0,-1,-1],
        [-1,-1,-1,-1,9,6,-1,0,1],
        [-1,-1,-1,-1,-1,4,-1,1,0]]
graf = Graf()
for i in range(len(data)):
    for j in range(len(data[i])):
        graf.addEdge(i,j,data[i][j])
graf.ostTreeLenKrasal()
graf.ostTreeLenPrima()
