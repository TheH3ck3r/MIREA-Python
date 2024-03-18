def smalldet(matrix: list):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

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

def det(matrix: list, i: int = 0):
    if len(matrix) == 2:
        return smalldet(matrix)
    else:
        opr = 0
        for j, elem in enumerate(matrix[0]):
            opr += ((-1) ** j) * elem * det(submatrix(matrix, i=i, j=j))
        return opr
def minor(matrix: list, i: int, j:int):
    return det(submatrix(matrix, i, j))

def alg(matrix: list, i: int, j: int):
    return ((-1)**(i+j)) * minor(matrix, i, j)

#---------------------------------------------------------------------------

def algmatrix(matrix: list):
    a = []
    for i in range(len(matrix)):
        a.append([])
        for j in range(len(matrix[i])):
            a[i].append(alg(matrix=matrix, i=i, j=j))
    return a

print(algmatrix(matrix=[[0, 2, 1, 4], [1, 0, 3, 2], [0, 1, 4, 0], [1, 2, 1, 1]]))