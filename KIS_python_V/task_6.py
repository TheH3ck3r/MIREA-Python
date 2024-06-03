import math


def main(l_b: set):
    e_big = {math.fabs(l_s) + l_s % 2 for l_s in l_b if l_s < 80}

    b_b = {math.fabs(e_s) - 9 * e_s for e_s in e_big if e_s <= 75}

    p_big = {8 * l_s for l_s in l_b if (-73 <= l_s or l_s <= 74)}

    h_big = {math.floor(p_s / 6) + math.fabs(e_s) for p_s in p_big
             for e_s in e_big if p_s > e_s}

    o_b = {math.fabs(h_small) - 5 * h_small for h_small in h_big
           if (h_small < -6) ^ (h_small >= -86)}

    v = len(b_b.union(o_b))
    - sum(b_s - 6 * o_s for b_s in b_b for o_s in o_b)
    return int(v)
