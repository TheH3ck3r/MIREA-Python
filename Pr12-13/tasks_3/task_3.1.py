from math import sqrt


def euclidean_distance(p1, p2):
    print("Внимание! Выполняются дорогостоящие вычисления!")
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


if __name__ == '__main__':
    distance = euclidean_distance((0, 0), (3, 4))
    print(distance)  # Должно быть 5
