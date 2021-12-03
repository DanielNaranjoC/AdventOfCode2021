import re
f = open('input.txt')
contar = []
t = 0
for i in f:
    if len(contar) == 0:
        contar = len(i) * [0]
    t = t + 1
    v = [int(i) for i in re.findall('([0-9])', i)]
    contar = [contar[i] + v[i] for i in range(len(v))]
p = [i/t for i in contar]
gamma = ''
epsilon = ''
for i in p:
    if i > 0.5:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
f.close()
print('Power: ', int(gamma, 2)*int(epsilon, 2))


f = open('input.txt')
numbers = [i for i in f]
ox = numbers
co = numbers
for i in range(len(numbers[0])-1):
    c = [int(j[i]) for j in ox]
    c = sum(c)/len(ox)
    if c >= 0.5:
        ox = [j for j in ox if j[i] == '1']
    else:
        ox = [j for j in ox if j[i] == '0']
    if len(ox) == 1:
        break

for i in range(len(numbers[0])-1):
    c = [int(j[i]) for j in co]
    c = sum(c)/len(co)
    if c >= 0.5:
        co = [j for j in co if j[i] == '0']
    else:
        co = [j for j in co if j[i] == '1']
    if len(co) == 1:
        break
f.close()
print('Life support rating:', int(ox[0], 2)*int(co[0], 2))
