from Extras.functions import *
import networkx as nx
import pandas as pd


matrix, nf, nc = read_matrix('input.txt')

g = nx.DiGraph()
edges_l = []
for i in matrix.keys():
    g.add_node(i)
    y, x = i
    if (y + 1, x) in matrix.keys():
        edges_l.append((i, (y + 1, x), matrix[(y + 1, x)]))
    if (y, x + 1) in matrix.keys():
        edges_l.append((i, (y, x + 1), matrix[(y, x + 1)]))
g.add_weighted_edges_from(edges_l)

print('Risk: ', nx.dijkstra_path_length(g, (0, 0), (nf - 1, nc - 1)))

n_matrix = {}
for i in range(nf):
    n_matrix[i] = {}
    for j in range(nc):
        n_matrix[i][j] = matrix[j, i]

data = pd.DataFrame(n_matrix)

times = 5

n_d = times * [data]
for i in range(1, times):
    n_d[i] = n_d[i - 1] + 1
    n_d[i][n_d[i] > 9] = 1
data = pd.concat(n_d, ignore_index=True)

n_d = times * [data]
for i in range(1, times):
    n_d[i] = n_d[i - 1] + 1
    n_d[i][n_d[i] > 9] = 1
data = pd.concat(n_d, axis=1, ignore_index=True)

g1 = nx.DiGraph()
edges_l = []
index = pd.MultiIndex.from_product([range(times * nf), range(times * nf)])
for i in index:
    g1.add_node(i)
    y, x = i
    if (y + 1, x) in index:
        edges_l.append((i, (y + 1, x), data.loc[y + 1, x]))
    if (y, x + 1) in index:
        edges_l.append((i, (y, x + 1), data.loc[y, x + 1]))
    if (y - 1, x) in index:
        edges_l.append((i, (y - 1, x), data.loc[y - 1, x]))
    if (y, x - 1) in index:
        edges_l.append((i, (y, x - 1), data.loc[y, x - 1]))
g1.add_weighted_edges_from(edges_l)

print('Risk: ', nx.dijkstra_path_length(g1, (0, 0), (times * nf - 1, times * nf - 1)))
