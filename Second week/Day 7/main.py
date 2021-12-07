import re


def mean(x_):
    return sum(x_) / len(x_)


f = open('input.txt')
x = re.findall('([0-9]+),*', f.read())
x = [int(i) for i in x]
f.close()

y = []
min_f = 1e+10
for i in range(min(x), max(x)):
    y.append([])
    for j in x:
        y[-1].append(abs(i-j))
    if sum(y[-1]) < min_f:
        min_f = sum(y[-1])

print('Min 1: ', min_f)

y = []
min_f = 1e+10
for i in range(min(x), max(x)):
    y.append([])
    for j in x:
        aux = abs(i-j)
        y[-1].append(sum([i for i in range(aux+1)]))
    if sum(y[-1]) < min_f:
        min_f = sum(y[-1])

print('Min 2: ', min_f)
