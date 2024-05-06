class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


get_inheritance = lambda cls: ' -> '.join(
    [cls.__name__] +
    get_inheritance(cls.__base__).split(' -> ') if cls.__base__ else [cls.__name__]
    )


def main():
    print(get_inheritance(C))


if __name__ == '__main__':
    main()