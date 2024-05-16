class MealyMachine:
    
    def __init__(self):
        self.state = 'A'

    def glare(self):
        match self.state:
            case "A":
                self.state = "B"
                return 0
            case "B":
                self.state = "B"
                return 2
            case "C":
                self.state = "A"
                return 4
            case "D":
                self.state = "E"
                return 5
            case "F":
                self.state = "G"
                return 8
            case _:
                raise MealyError("glare")

    def place(self):
        match self.state:
            case "B":
                self.state = "C"
                return 1
            case "C":
                self.state = "D"
                return 3
            case "D":
                self.state = "A"
                return 6
            case "E":
                self.state = "F"
                return 7
            case "F":
                self.state = "C"
                return 9
            case _:
                raise MealyError("place")


class MealyError(Exception):

    def __init__(self, method_name):
        self.method_name = method_name


def main():
    return MealyMachine()


def test():
    o = main()
    try:
        o.place()
    except MealyError:
        pass
    o.glare()