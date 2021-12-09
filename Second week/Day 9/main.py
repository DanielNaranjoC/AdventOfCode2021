import re


def is_lower(f, c, matrix, tf, tc):
    low = True
    if f + 1 < tf:
        low = low and (matrix[f + 1][c] > matrix[f][c])
    if f - 1 > -1:
        low = low and (matrix[f - 1][c] > matrix[f][c])
    if c - 1 > -1:
        low = low and (matrix[f][c - 1] > matrix[f][c])
    if c + 1 < tc:
        low = low and (matrix[f][c + 1] > matrix[f][c])
    return low


def find_basin(f, c, matrix, tf, tc, x_i):
    x = x_i.copy()
    if f + 1 < tf:
        if matrix[f + 1][c] != 9:
            x.add((f + 1, c))
    if f - 1 > -1:
        if matrix[f - 1][c] != 9:
            x.add((f-1, c))
    if c - 1 > -1:
        if matrix[f][c - 1] != 9:
            x.add((f, c - 1))
    if c + 1 < tc:
        if matrix[f][c + 1] != 9:
            x.add((f, c + 1))
    if x == x_i:
        return True
    else:
        x_i.update(x)
        for f1, c1 in x:
            find_basin(f1, c1, matrix, tf, tc, x_i)


file = open('input.txt')
n = []
for i in file:
    t = re.findall('([0-9])', i)
    n.append([int(i) for i in t])
file.close()

if len(n) > 0:
    filas = len(n)
    columnas = len(n[0])
    number = []
    positions = []
    for i in range(filas):
        for j in range(columnas):
            if is_lower(i, j, n, filas, columnas):
                number.append(n[i][j])
                positions.append((i, j))
    s = sum([i + 1 for i in number])
    print('Risk: ', s)
    basin_l = []
    for i in positions:
        pos_b = {i}
        find_basin(i[0], i[1], n, filas, columnas, pos_b)
        basin_l.append(pos_b)
    basin_l = list(basin_l)
    basin_l.sort(key=len, reverse=True)
    p = 1
    for i in range(3):
        p = p * len(basin_l[i])
    print('Prod: ', p)



