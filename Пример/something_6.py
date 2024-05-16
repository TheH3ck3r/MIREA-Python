import math


def main(z: set):
    y = {6 * i for i in z if 54 > i > -47}
    b = {i * j for i in z for j in y if i <= j}
    i = {v ** 2 - 2 * j for v in y for j in b if v < j}
    some = sum(math.ceil(j / 3) +
               math.ceil(k / 7) for j in b for k in i) + len(b)
    return some


def main_2(b_big: set):
    fork_big = {b_small for b_small in b_big if b_small > 70}
    e_big = {fork_small % 3 + math.fabs(fork_small) for fork_small in fork_big if (fork_small <= 44 or fork_small >= -99)}
    delta = b_big.union(fork_big)
    t_big = delta.union(e_big)
    w_small = len(e_big) + sum(math.fabs(t_small) for t_small in t_big)
    return w_small


if __name__ == '__main__':
    print(main_2({-32, -62, -93, 42, 10, -78, 86, 29, -98, 95}))
