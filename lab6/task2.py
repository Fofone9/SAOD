class Struct:
    def __init__(self):
        self.node = dict()

    def transformation(self, g, h):
        for i in range(len(g)):
            if g[i] not in self.node.keys():
                self.node[g[i]] = list()
            self.node[g[i]].append(h[i])
        # for i in h:
        #     if i not in self.node.keys():
        #         self.node[i] = '0'

    def show(self):
        for i in self.node.keys():
            print(i, '-', ', '.join(self.node[i]))


st = Struct()
g = ('a','a','a','b','d','d','e','e','f','f','g')
h = ('b','e','f','c','c','g','d','f','d','g','c')
st.transformation(g, h)
print(g)
print(h)
print()
st.show()
