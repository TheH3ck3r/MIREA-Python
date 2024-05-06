import deal
from math import sqrt

distance_function = deal.chain(
    deal.pre(lambda p1, p2: p1 is not None and p2 is not None),
    deal.pre(lambda p1, p2: len(p1) != 0 and len(p2) != 0),
    deal.pre(lambda p1, p2: (type(p1) == tuple or type(p1) == list) and (type(p2) == tuple or type(p2) == list)),
    deal.pre(lambda p1, p2: len(p1) == len(p2)),
    deal.pre(lambda p1, p2: all(isinstance(i, float | int) for i in p1 + p2)),
    deal.has(),
    deal.post(lambda result: isinstance(result, float | int)),
    deal.post(lambda result: result >= 0))


@distance_function
def manhattan_distance(p1, p2):
    """
    >>> manhattan_distance([0, 0], [3, 4])
    7
    """
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


@distance_function
def euclidean_distance(p1, p2):
    """
    >>> euclidean_distance([0, 0], [3, 4])
    5.0
    """
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


if __name__ == '__main__':
    distance = euclidean_distance((0, 0), (3, 4))
    print(distance)
