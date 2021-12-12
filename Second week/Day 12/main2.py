import re
import networkx as nx


nodes = set()
edges = []
f = open('input.txt')
for i in f:
    aux = re.findall('([A-z]+)-([A-z]+)', i)
    edges.append(aux[0])
    nodes.union(set(aux[0]))
f.close()
g = nx.Graph()
for i in nodes:
    g.add_node(i)
for i, j in edges:
    g.add_edge(i, j)

st = 'start'
r = 0
end = 'end'
# position, cant_visit, twice
paths = [(st, [st], [])]
c = 0
while len(paths) > 0: # and c < 1000:
    # print('All: ', paths)
    pos, cant_visit, repeat = paths[0]
    paths = paths[1:]
    # print('Pos: ', pos)
    # print('Cant: ', cant_visit)
    if pos == end:
        r += 1
        continue
    for i in g.neighbors(pos):
        if i not in cant_visit:
            cant_visit_ = cant_visit.copy()
            if i.lower() == i:
                cant_visit_.append(i)
            paths.append((i, cant_visit_, repeat.copy()))
        elif i not in [end, st] + repeat and len(repeat) < 1:
            # print('rep: ', i)
            paths.append((i, cant_visit.copy(), repeat + [i]))
    c += 1
print('Paths: ', r)
