import deal
from math import sqrt
from some import raises


# def euclidean_distance(p1, p2):
#     print("Внимание! Выполняются дорогостоящие вычисления!")
#     return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


@deal.pre(lambda p1, p2: p1 is not None and p2 is not None)
@deal.pre(lambda p1, p2: len(p1) != 0 and len(p2) != 0)
@deal.pre(lambda p1, p2: (type(p1) == tuple or type(p1) == list) and (type(p2) == tuple or type(p2) == list))
@deal.pre(lambda p1, p2: len(p1) == len(p2))
@deal.pre(lambda p1, p2: all(isinstance(i, float | int) for i in p1 + p2))
@deal.has()
@deal.post(lambda result: isinstance(result, float | int))
def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def test_error():
    with raises(deal.PostContractError):
        euclidean_distance([0, 0], [3, 4])


if __name__ == '__main__':
    distance = euclidean_distance((0, 0), (3, 4))
    print(distance)
