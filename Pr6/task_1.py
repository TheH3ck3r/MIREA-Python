def smalldet(matrix: list):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

print(smalldet(matrix=[[4, 3], [1, 1]]))