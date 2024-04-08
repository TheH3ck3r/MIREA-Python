class MyClass:
    def __init__(self):
        self.name = "Mikel"

    def greet(self):
        print(f"Hello, my name is {self.name}")


def main():
    obj = MyClass()

    method_name = "greet"
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        method()
    else:
        print(f"Method {method_name} not found in the object")


if __name__ == '__main__':
    main()
    