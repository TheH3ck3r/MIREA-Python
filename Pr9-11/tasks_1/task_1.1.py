class MyClass:
    def __init__(self):
        self.name = "Mikel"
        self.age = 19
        self.__secret = "I have a secret"


def main():
    obj = MyClass()

    for attr in vars(obj):
        if not "__" in attr:
            print(attr)
        else:
            some = attr.split("__")
            print(some[len(some)-1])


if __name__ == '__main__':
    main()