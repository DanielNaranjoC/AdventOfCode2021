import re

f = open('input.txt')
fish = re.findall('([0-9]+),*', f.read())
values = [int(i) for i in fish]
fish = {}
for i in values:
    if i in fish.keys():
        fish[i] += 1
    else:
        fish[i] = 1
f.close()
days = 256
for i in range(days):
    n_fish = {i: 0 for i in range(9)}
    for j in fish.keys():
        if j == 0:
            n_fish[8] = n_fish[8] + fish[j]
            n_fish[6] = n_fish[6] + fish[j]
        else:
            n_fish[j-1] = n_fish[j-1] + fish[j]
    fish = n_fish
print('Hay,', sum(fish.values()), 'peces.')
