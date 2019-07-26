# -*- coding: utf-8 -*-


def pathInMatrix(matrix: str, rows: int, cols: int, path: str) -> 'bool':
    if matrix and rows > 0 and cols > 0 and path:
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if pathInCore(list(matrix), rows, cols, i, j, path[1:]):
                        return True
    return False


def pathInCore(matrix: str, rows: int, cols: int, i: int, j: int, path: str) -> 'bool':
    if not path:
        return True
    matrix[i * cols + j] = '-' # prevent going back to the same tile
    flag = False
    for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
        if 0 <= x < rows and 0 <= y < cols and \
            matrix[x * cols + y] == path[0]:
            if pathInCore(matrix, rows, cols, x, y, path[1:]):
                flag = True
    return flag


if __name__ == '__main__':
    print(pathInMatrix('ABEESFCSADME', rows=3, cols=4, path='SEE'))
    print(pathInMatrix('abtgcfcsjdeh', rows=3, cols=4, path='bfce'))
    print(pathInMatrix('abtgcfcsjdeh', rows=3, cols=4, path='abfb'))
    print(pathInMatrix('ABCESFCSADEE', rows=3, cols=4, path='SEE'))
    print(pathInMatrix('ABCESFCSAEEE', rows=3, cols=4, path='ABCESEEEFS'))
