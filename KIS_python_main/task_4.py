def main(n):
    if n == 0:
        return -0.81
    elif n == 1:
        return -0.46
    elif n >= 2:
        value = 1 - ((main(n - 1)) ** 2) - (main(n - 2) / 6) \
                - 0.06 - ((main(n - 1)) ** 2)
    return value


if __name__ == '__main__':
    print(main(5))