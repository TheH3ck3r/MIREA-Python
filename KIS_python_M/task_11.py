class MealyMachine:

    def __init__(self):
        self.state = 'A'

    def init(self):
        match self.state:
            case "A":
                self.state = "A"
                return 1
            case "B":
                self.state = "C"
                return 3
            case "D":
                self.state = "E"
                return 5
            case "E":
                self.state = "F"
                return 8
            case _:
                raise MealyError("init")

    def run(self):
        match self.state:
            case "A":
                self.state = "B"
                return 0
            case "D":
                self.state = "B"
                return 6
            case _:
                raise MealyError("run")

    def rev(self):
        match self.state:
            case "A":
                self.state = "D"
                return 2
            case "C":
                self.state = "D"
                return 4
            case "D":
                self.state = "D"
                return 7
            case _:
                raise MealyError("rev")


class MealyError(Exception):

    def __init__(self, method_name):
        self.method_name = method_name


def main():
    return MealyMachine()


def test():
    o = main()
    o.init()
    o.run()
    try:
        o.run()
    except MealyError:
        pass
    try:
        o.rev()
    except MealyError:
        pass
    o.init()
    try:
        o.init()
    except MealyError:
        pass
    o.rev()
    o.run()

    o.state = "A"
    o.rev()
    o.rev()
    o.init()
    o.init()
