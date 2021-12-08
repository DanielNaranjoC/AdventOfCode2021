import re
import itertools

numbers_d = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
numbers_c = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
numbers_use = [1, 7, 4, 8]
long = [numbers_d[i] for i in numbers_use]
perms = list(itertools.permutations('abcdefg'))


def get_options(decoded):
    pos_0 = list(set(decoded[7]) - set(decoded[1]))[0]
    one = list(decoded[1])
    will_try = []
    for i in perms:
        pos_1 = ((i[2] == one[0] and i[5] == one[1]) or (i[2] == one[1] and i[5] == one[0]))
        pos_2 = list(set(decoded[4]) - set(decoded[1]))
        pos_2 = ((i[1] == pos_2[0] and i[3] == pos_2[1]) or (i[1] == pos_2[1] and i[3] == pos_2[0]))
        pos_3 = list((set(decoded[8]) - set(decoded[7])) - set(decoded[4]))
        pos_3 = ((i[4] == pos_3[0] and i[6] == pos_3[1]) or (i[4] == pos_3[1] and i[6] == pos_3[0]))
        if i[0] == pos_0 and pos_1 and pos_2 and pos_3:
            will_try.append(i)
    return will_try


def decode(decoded, right_):
    aux = get_options(decoded)
    for positions in aux:
        w_use = 'abcdefg'
        w_use = {w_use[i]: positions[i] for i in range(7)}
        numbers_decoded = numbers_c.copy()
        for i in range(len(numbers_decoded)):
            n = [i for i in numbers_decoded[i]]
            for j in range(len(n)):
                n[j] = w_use[n[j]]
            n = ''.join(n)
            numbers_decoded[i] = n
        new_numbers = []
        for i in right_:
            for j in range(len(numbers_decoded)):
                if set(i) == set(numbers_decoded[j]):
                    new_numbers.append(j)
        if len(new_numbers) == 4:
            return int(''.join([str(i) for i in new_numbers]))
    print('No')
    return 0


f = open('input.txt')

count = 0
s = 0
for i in f:
    decoded_ = {}
    t = i.split('|')
    left = re.findall('([a-g]+),*', t[0])
    use = []
    for j in left:
        if len(j) in long:
            use.append(j)
            d = numbers_d.index(len(j))
            if d not in decoded_.keys():
                decoded_[d] = j
    right = re.findall('([a-g]+),*', t[1])
    aux = decode(decoded_, right)
    s = s + aux
    final = []
    for j in right:
        for k in use:
            if set(j) == set(k):
                final.append(j)
                break
    count = count + len(final)
f.close()
print('Count: ', count)
print('Sum: ', s)

