def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"original (rows, cols): {rows}, {cols}")
    t=[[0] * rows for _ in range(cols)]
    print(f"Empty new matrix t: {t}")
    for i in range(rows):
        for j in range(cols):
            t[j][i]=matrix[i][j]
    return t


matrix = [[1,2],[3,4],[5,6],[7,8]]
print(matrix)
transposed = transpose(matrix)
print(transposed)
