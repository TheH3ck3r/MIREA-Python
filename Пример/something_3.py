def main(b, n, a):
    sum_1 = 1
    for i in range(1, b + 1):
        sum_1 *= (0.01 + i ** 3 / 54) ** 4
    sum_2 = 1
    for c in range(1, a + 1):
        sum_3 = 0
        for j in range(1, n + 1):
            sum_3 += 48*c**5 - 47*(37*j-j**3-77)
        sum_2 *= sum_3
    result = sum_1-sum_2
    return result


if __name__ == '__main__':
    print(main(2, 4, 6))
