def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        stolb = []
        matrix.append(stolb)
        for _ in range(m):
            stolb.append(value)
    return matrix
result1 = get_matrix(3, 7, 13)
print(result1)