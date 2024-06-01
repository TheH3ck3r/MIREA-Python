class MealyMachine:

    def __init__(self):
        self.state = 'A'

    def sway(self):
        match self.state:
            case "A":
                self.state = "B"
                return 0
            case "C":
                self.state = "D"
                return 2
            case "F":
                self.state = "A"
                return 7
            case _:
                raise MealyError("sway")

    def spin(self):
        match self.state:
            case "B":
                self.state = "C"
                return 1
            case "D":
                self.state = "E"
                return 3
            case "F":
                self.state = "G"
                return 6
            case "G":
                self.state = "C"
                return 9
            case _:
                raise MealyError("spin")

    def click(self):
        match self.state:
            case "D":
                self.state = "B"
                return 4
            case "E":
                self.state = "F"
                return 5
            case "F":
                self.state = "B"
                return 8
            case _:
                raise MealyError("click")


class MealyError(Exception):

    def __init__(self, method_name):
        self.method_name = method_name


def main():
    return MealyMachine()


def test():
    o = main()
    try:
        o.spin()
    except MealyError:
        pass
    try:
        o.click()
    except MealyError:
        pass
    o.sway()
    o.spin()
    o.sway()
    try:
        o.sway()
    except MealyError:
        pass
    o.click()

    o.state = "D"
    o.spin()
    o.click()
    o.click()

    o.state = "F"
    o.sway()

    o.state = "F"
    o.spin()
    o.spin()