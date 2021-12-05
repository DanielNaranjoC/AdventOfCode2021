import re

f = open('input.txt')
lines_str = []
lines = []
mx = 0
my = 0
for i in f:
    x = re.search('([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)', i)
    x = [int(x.group(j)) for j in range(1, 5)]
    lines_str.append([(x[0], x[1]), (x[2], x[3])])
for p1, p2 in lines_str:
    lines.append([p1, p2])
    mx = max(mx, p1[0], p2[0])
    my = max(my, p1[1], p2[1])

matrix = (my + 1) * [(mx + 1) * [0]]
matrix = [i.copy() for i in matrix]
for p1, p2 in lines:
    if p1[0] == p2[0]:
        for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            matrix[i][p1[0]] = matrix[i][p1[0]] + 1
    elif p1[1] == p2[1]:
        for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            matrix[p1[1]][i] = matrix[p1[1]][i] + 1
s = 0
for i in matrix:
    for j in i:
        if j > 1:
            s = s + 1
f.close()

print('Points: ', s)

matrix2 = (my + 1) * [(mx + 1) * [0]]
matrix2 = [i.copy() for i in matrix2]
for p1, p2 in lines:
    if p1[0] == p2[0]:
        for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            matrix2[i][p1[0]] = matrix2[i][p1[0]] + 1
    elif p1[1] == p2[1]:
        for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            matrix2[p1[1]][i] = matrix2[p1[1]][i] + 1
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        if abs(m) == 1:

            def r(p):
                return int(m * (p - p2[0]) + p2[1])


            if p2 == (2, 0):
                print(matrix2)
            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                matrix2[r(i)][i] = matrix2[r(i)][i] + 1


s = 0
for i in matrix2:
    for j in i:
        if j > 1:
            s = s + 1

print('Points: ', s)
