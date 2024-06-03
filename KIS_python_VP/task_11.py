class MealyMachine:

    def __init__(self):
        self.state = 'A'

    def wreck(self):
        match self.state:
            case "A":
                self.state = "B"
                return 0
            case "G":
                self.state = "C"
                return 9
            case "H":
                self.state = "D"
                return 11
            case _:
                raise MealyError("wreck")

    def coat(self):
        match self.state:
            case "B":
                self.state = "C"
                return 1
            case "C":
                self.state = "D"
                return 2
            case "F":
                self.state = "A"
                return 6
            case "G":
                self.state = "E"
                return 8
            case _:
                raise MealyError("coat")

    def cast(self):
        match self.state:
            case "D":
                self.state = "E"
                return 3
            case "E":
                self.state = "F"
                return 4
            case _:
                raise MealyError("cast")

    def trace(self):
        match self.state:
            case "F":
                self.state = "G"
                return 5
            case "G":
                self.state = "H"
                return 7
            case "H":
                self.state = "F"
                return 10
            case _:
                raise MealyError("trace")


class MealyError(Exception):

    def __init__(self, method_name):
        self.method_name = method_name


def main():
    return MealyMachine()

def test():
    o = main()
    try:
        o.coat()
    except MealyError:
        pass
    try:
        o.cast()
    except MealyError:
        pass
    try:
        o.trace()
    except MealyError:
        pass
    o.wreck()
    try:
        o.wreck()
    except MealyError:
        pass
    o.coat()
    o.coat()
    o.cast()
    o.cast()
    o.coat()

    o.state = "F"
    o.trace()
    o.coat()

    o.state = "G"
    o.wreck()

    o.state = "G"
    o.trace()
    o.trace()

    o.state = "H"
    o.wreck()
