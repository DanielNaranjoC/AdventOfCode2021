import re


def read_matrix(filename):
    f = open(filename)
    nf = 0
    nc = 0
    x = []
    for i in f:
        aux = re.findall('([0-9])', i)
        x.append([int(i) for i in aux])
        nf += 1
        nc = max(nc, len(aux))
    m = {}
    for i in range(nf):
        for j in range(nc):
            m[i, j] = x[i][j]
    return m
