import re

f = open('input.txt')
numbers = re.findall('([0-9]+),*', f.readline())
cards = []
for i in f:
    c = re.findall('([0-9]+)', i)
    if len(c) == 0:
        continue
    if len(cards) == 0:
        cards.append([c])
    elif len(cards[-1]) == 5:
        cards.append([c])
    else:
        cards[-1].append(c)
f.close()


def create_c(card):
    c = [[(i, 0) for i in j] for j in card]
    return c


def check_card(card):
    for i in card:
        x = sum([j[1] for j in i])
        if x == 5:
            return True
    for i in range(5):
        x = sum([j[i][1] for j in card])
        if x == 5:
            return True
    return False


def change_card(card, v):
    for i in range(5):
        for j in range(5):
            if card[i][j][0] == v:
                card[i][j] = (v, 1)


def sum_card(card):
    s = 0
    for i in range(5):
        for j in range(5):
            if card[i][j][1] == 0:
                s = s + int(card[i][j][0])
    return s


cards_j = [create_c(i) for i in cards]
w = False
for i in numbers:
    for j in cards_j:
        change_card(j, i)
    for j in cards_j:
        if check_card(j):
            p = sum_card(j)
            print('Win: ', int(i) * p)
            w = True
            break
    if w:
        break

cards_j = [create_c(i) for i in cards]
win_r = []
for i in numbers:
    for j in cards_j:
        change_card(j, i)
    delete = []
    for j in range(len(cards_j)):
        if check_card(cards_j[j]):
            win_r.append((cards_j[j].copy(), i))
            delete.append(cards_j[j])
    for j in delete:
        cards_j.remove(j)
            
p = sum_card(win_r[-1][0])
print('Loose: ', int(win_r[-1][1]) * p)
