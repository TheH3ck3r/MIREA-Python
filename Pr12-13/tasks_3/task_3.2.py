import deal
from math import sqrt
from some import raises


def euclidean_distance(p1, p2):
    print("Внимание! Выполняются дорогостоящие вычисления!")
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


@deal.pre(lambda p1, p2: p1 is not None and p2 is not None)
def euclidean_distance(p1, p2):
    print("Внимание! Выполняются дорогостоящие вычисления!")
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def test_error():
    with raises(deal.PreContractError):
        euclidean_distance(None, None)


if __name__ == '__main__':

    distance = euclidean_distance((0, 0), (3, 4))
    print(distance)


