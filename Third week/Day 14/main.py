import re


f = open('input.txt')
first = f.readline()[:-1]
chain = first
change = {}
for i in f:
    aux = re.findall('([A-Z]+) -> ([A-Z]+)', i)
    if len(aux) > 0:
        x, y = aux[0]
        change[x] = y
f.close()

count_pair = {i: 0 for i in change.keys()}
for i in range(len(first)-1):
    count_pair[first[i:i + 2]] += 1
steps = 40
for _ in range(steps):
    count_pair_aux = {i: 0 for i in change.keys()}
    for i in count_pair.keys():
        key_1 = i[0] + change[i]
        key_2 = change[i] + i[1]
        count_pair_aux[key_1] += count_pair[i]
        count_pair_aux[key_2] += count_pair[i]
    count_pair = count_pair_aux

count_letter = {}
for i in count_pair.keys():
    if i[0] in count_letter.keys():
        count_letter[i[0]] += count_pair[i]
    else:
        count_letter[i[0]] = count_pair[i]
if first[-1] in count_letter:
    count_letter[first[-1]] += 1
else:
    count_letter[first[-1]] = 1
count_letter = {i: count_letter[i] for i in count_letter if count_letter[i] > 0}
print('Range: ', max(count_letter.values()) - min(count_letter.values()))

