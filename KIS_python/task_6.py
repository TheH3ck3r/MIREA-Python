import math


# 
def main(z: set):
    y = {6 * i for i in z if 54 > i > -47}
    b = {i * j for i in z for j in y if i <= j}
    i = {v ** 2 - 2 * j for v in y for j in b if v < j}
    some = sum(math.ceil(j / 3) +
               math.ceil(k / 7) for j in b for k in i) + len(b)
    return some