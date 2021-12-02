import re
f = open('input.txt')
h = 0
p = 0
for i in f:
    x = re.search('([0-9]+)', i)
    n = int(x.group(0))
    if 'forward' in i:
        h = h + n
    if 'down' in i:
        p = p + n
    if 'up' in i:
        p = p - n
f.close()
print('Product: ', p*h)


f = open('input.txt')
h = 0
a = 0
p = 0
for i in f:
    x = re.search('([0-9]+)', i)
    n = int(x.group(0))
    if 'forward' in i:
        h = h + n
        p = p + a * n
    if 'down' in i:
        a = a + n
    if 'up' in i:
        a = a - n
f.close()
print('Product: ', p * h)

