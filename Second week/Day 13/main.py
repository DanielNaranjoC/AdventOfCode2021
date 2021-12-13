from Extras.functions import *


def print_m(m_, nf_, nc_):
    for i in range(nf_):
        for j in range(nc_):
            print(m_[i, j], end=' ')
        print()


def complete_matrix(m_, nf_, nc_):
    for i in range(nf_):
        for j in range(nc_):
            if (i, j) not in m_.keys():
                m_[i, j] = '.'


# def read_file(filename):
f = open('input.txt')
nf = 0
nc = 0
m = {}
inst = []
for i in f:
    aux = re.findall('([0-9]+),([0-9]+)', i)
    if len(aux) > 0:
        m[int(aux[0][1]), int(aux[0][0])] = '*'
        nf = max(nf, int(aux[0][1])+1)
        nc = max(nc, int(aux[0][0])+1)
    elif i != '\n':
        inst.append(i)
f.close()

complete_matrix(m, nf, nc)
# print_m(m, nf, nc)


# print('\n\n\n')
for k in range(len(inst)):
    i = inst[k]
    i = re.findall('([xy])=([0-9]+)', i)
    if len(i) > 0:
        n_m = {}
        i = i[0]
        if i[0] == 'y':
            m_row = nf - 1
            pos = int(i[1])
            m_row = min(m_row - 1, pos)
            for row in range(1, m_row + 1):
                y1 = pos - row
                y2 = pos + row
                if y2 >= nf:
                    continue
                for col in range(nc):
                    if m[y1, col] == '*' or m[y2, col] == '*':
                        n_m[y1, col] = '*'
                    else:
                        n_m[y1, col] = '.'
            nf = min(pos, m_row)
            complete_matrix(n_m, nf, nc)
            # print_m(n_m, pos, nc)

        elif i[0] == 'x':
            m_col = nc - 1
            pos = int(i[1])
            m_col = min(m_col, pos)
            for col in range(1, m_col + 1):
                x1 = pos - col
                x2 = pos + col
                if x2 >= nc:
                    continue
                for row in range(nf):
                    if m[row, x1] == '*' or m[row, x2] == '*':
                        n_m[row, x1] = '*'
                    else:
                        n_m[row, x1] = '.'
            nc = min(pos, m_col)
            complete_matrix(n_m, nf, nc)
            # print_m(n_m, nf, pos)
        if k == 0:
            c = 0
            for i in n_m.keys():
                if n_m[i] == '*':
                    c += 1
            print('Count 1: ', c)
        m = n_m


print('Code: ')
print_m(m, nf, nc)

