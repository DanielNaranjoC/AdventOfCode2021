import multiprocessing as mp
import itertools


def walk(v, target_x, target_y, print_r=False):
    if v[0] == 0:
        return
    t_x = 0
    t_y = 0
    high = 0
    length = 0
    n = 0
    vx = v[0]
    vy = v[1]
    while True:
        if target_x[0] <= t_x <= target_x[1] and target_y[0] <= t_y <= target_y[1]:
            break
        t_x = t_x + vx
        t_y = t_y + vy - n
        high = max(high, t_y)
        length = max(length, t_x)
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        n += 1
        if t_y < target_y[0] or t_x > target_x[1] + 1:
            return
    if print_r:
        print(t_x)
        print(t_y)
        print('Steps: ', n)
    return n, length, high


lx = [155, 215]
ly = [-132, -72]


def my_f(v):
    return walk(v, lx, ly)


if __name__ == '__main__':
    pool = mp.Pool()
    r = pool.map(my_f, itertools.product(range(-500, 500), range(-500, 500)))
    r = [i for i in r if i is not None]
    max_high = 0
    for i, j, k in r:
        max_high = max(max_high, k)
    print('High: ', max_high)
    print('Count: ', len(r))

