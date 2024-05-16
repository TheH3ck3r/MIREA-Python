class MealyMachine:

    def __init__(self):
        self.state = 'A'

    def close(self):
        match self.state:
            case 'A':
                self.state = 'B'
                return 0
            case 'B':
                self.state = 'F'
                return 4
            case 'G':
                self.state = 'H'
                return 9
            case 'H':
                self.state = 'A'
                return 11
            case _:
                raise MealyError("close")

    def rev(self):
        match self.state:
            case 'B':
                self.state = 'C'
                return 2
            case 'D':
                self.state = 'E'
                return 6
            case 'F':
                self.state = 'G'
                return 8
            case _:
                raise MealyError("rev")

    def pull(self):
        match self.state:
            case 'A':
                self.state = 'E'
                return 1
            case 'B':
                self.state = 'H'
                return 3
            case 'C':
                self.state = 'D'
                return 5
            case 'E':
                self.state = 'F'
                return 7
            case 'G':
                self.state = 'A'
                return 10
            case _:
                raise MealyError("pull")


class MealyError(Exception):

    def __init__(self, method_name):
        self.method_name = method_name


def main():
    return MealyMachine()


def test():
    o = main()
    try:
        o.rev()
    except MealyError:
        pass
    o.close()
    o.pull()
    try:
        o.pull()
    except MealyError:
        pass
    o.close()
    o.state = 'B'
    o.close()
    try:
        o.close()
    except MealyError:
        pass
    o.rev()
    o.close()
    o.state = 'B'
    o.rev()
    o.pull()
    o.rev()
    o.pull()
    o.state = 'A'
    o.pull()

    o.state = 'G'
    o.pull()
