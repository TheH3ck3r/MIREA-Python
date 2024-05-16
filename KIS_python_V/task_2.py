import math


def main(x):
    if x < 76:
        answer = ((math.cos(x)**4)-(83*(math.sin(x))))
    elif 76 <= x < 165:
        answer = (87*math.log10(x))
    elif 165 <= x < 200:
        answer = (32*(math.fabs(((x**3)/8)+(57*x))**2))
    elif x >= 200:
        answer = ((36*((4+(x**3)+(x**2))**6))+0.05+((32*(x**3))**3))
    return answer


if __name__ == '__main__':
    print(main(213))
    print(main(216))
    print(main(195))
    print(main(175))