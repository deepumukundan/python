def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    t=[[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            t[j][i]=matrix[i][j]
    return t


matrix = [[1,2],[3,4],[5,6],[7,8]]
print(matrix)
transposed = transpose(matrix)
print(transposed)
