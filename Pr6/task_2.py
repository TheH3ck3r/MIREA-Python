def submatrix(matrix: list, i: int, j: int):
    res = []
    for row in enumerate(matrix):
        if row[0] != i:
            new_row = []
            for col in enumerate(row[1]):
                if col[0] != j:
                    new_row.append(col[1])
            res.append(new_row)
    return res

print(submatrix(matrix=[[0, 2, 1], [1, 4, 3], [2, 1, 1]], i = 0, j = 0))
print(submatrix(matrix=[[0, 2, 1], [1, 4, 3], [2, 1, 1]], i = 1, j = 1))
print(submatrix(matrix=[[0, 2, 1], [1, 4, 3], [2, 1, 1]], i = 2, j = 1))