file = open('input.txt')

incorrect = []
incomplete = []
open_c = '{([<'
close_c = {'{': '}', '(': ')', '[': ']', '<': '>', '': ''}
point = {'}': 1197, ')': 3, ']': 57, '>': 25137}
for i in file:
    opened = []
    is_incorrect = False
    for j in range(len(i)):
        if i[j] in close_c.values():
            if len(opened) == 0:
                incorrect.append(j)
                break
            elif i[j] != close_c[opened[-1]]:
                incorrect.append(i[j])
                is_incorrect = True
                break
            else:
                opened.pop()
        else:
            opened.append(i[j])
    if not is_incorrect:
        incomplete.append(i)

s = sum([point[i] for i in incorrect])
print('Incorrect: ', s)

all_news = []
for i in incomplete:
    opened = []
    for j in range(len(i)):
        if i[j] in close_c.values():
            opened.pop()
        else:
            opened.append(i[j])
    if '\n' in opened:
        opened.remove('\n')
    opened.reverse()
    all_news.append(opened)

scores = []
c_points = {')': 1, ']': 2, '}': 3, '>': 4}
for i in all_news:
    p = 0
    for j in i:
        p = 5*p + c_points[close_c[j]]
    scores.append(p)
scores.sort()
n = int(len(scores)/2)
print('Complete: ', scores[n])
