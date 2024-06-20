import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.Graph()

# Добавляем 14 вершин
num_vertices = 14
vertices = list(range(1, num_vertices + 1))

# Добавляем гамильтонов цикл
edges = [(i, i+1) for i in range(1, num_vertices)]
edges.append((num_vertices, 1))  # Замыкаем цикл

# Добавляем рёбра в граф
G.add_edges_from(edges)

# Добавляем дополнительные рёбра для усложнения структуры
additional_edges = [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, 10)]
G.add_edges_from(additional_edges)

# Рисуем граф
pos = nx.circular_layout(G)  # Располагаем вершины по окружности
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title("Граф с гамильтоновым циклом и 14 вершинами")
plt.show()
