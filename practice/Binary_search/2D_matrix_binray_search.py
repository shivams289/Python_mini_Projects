matrix = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]


def func(matrix, key):
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == key:
            return [i, j]

        elif matrix[i][j] > key:
            j -= 1

        else:
            i += 1
    return -1


print(func(matrix, 1))
