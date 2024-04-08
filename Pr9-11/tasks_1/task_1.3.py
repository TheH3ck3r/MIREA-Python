class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


def main():
    obj = C()


if __name__ == '__main__':
    main()