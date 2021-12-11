import re


def check_step(row, col, matrix_, t_row, t_col):
    matrix = [i.copy() for i in matrix_]
    # print(matrix, end='\n\n')
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j and i == 0:
                continue
            if (0 <= row + i < t_row) and (0 <= col + j < t_col):
                matrix[row + i][col + j] = matrix[row + i][col + j] + 1
    return matrix


def step(matrix, t_row, t_col):
    aux_v = [i.copy() for i in matrix]
    for i in range(t_row):
        for j in range(t_col):
            aux_v[i][j] += 1
    return aux_v


def update(matrix, t_row, t_col):
    z = 0
    for i in range(t_row):
        for j in range(t_col):
            if matrix[i][j] > 9:
                matrix[i][j] = 0
                z += 1
    return z


def one_run(matrix, t_row, t_col):
    matrix = step(matrix, t_row, t_col)
    len_e = 0
    exp = []
    while True:
        for r in range(t_col):
            for c in range(t_row):
                if matrix[r][c] > 9 and (r, c) not in exp:
                    matrix = check_step(r, c, matrix, t_row, t_col)
                    exp.append((r, c))
        if len(exp) == len_e:
            break
        else:
            len_e = len(exp)
    t = update(matrix, t_row, t_col)
    return t, matrix


x = []
y = []
f = open('input.txt')
n_col = 0
for line in f:
    n_col = max(n_col, len(line))
    aux = re.findall('([0-9])', line)
    x.append([int(i) for i in aux])
    y.append([int(i) for i in aux])
f.close()
n_row = len(x)
n_col = n_col - 1

flashes = 0
first = False
for count in range(100):
    tot_f, x = one_run(x, n_row, n_col)
    flashes = flashes + tot_f
print('Flashes: ', flashes)

count = 0
x = y
while not first:
    tot_f, x = one_run(x, n_row, n_col)
    if tot_f == n_col * n_row and not first:
        print('First: ', count + 1)
        first = True
    count += 1
