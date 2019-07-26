# -*- coding: utf-8 -*-


def getDigitSum(num: int) -> int:
    tot = 0
    while num > 0:
        tot += num % 10
        num //= 10
    return tot


def movingCount(threshold: int, rows: int, cols: int) -> int:
    if threshold > 0 and rows > 0 and cols > 0:
        visited = [[False] * cols for _ in range(rows)]
        return movingCountCore(threshold, rows, cols, 0, 0, visited)
    return 0


def _movingCount(threshold: int, rows: int, cols: int) -> int:
    if threshold > 0 and rows > 0 and cols > 0:
        visited = [[False] * cols for _ in range(rows)]
        return _movingCountCore(threshold, rows, cols, visited)
    return 0


def movingCountCore(threshold: int, rows: int, cols: int,
                    i: int, j: int, visited: 'matrix') -> int:
    '''
        tail recursion version, could exceed the maximum recursion depth
    '''
    count = 0
    if check(threshold, rows, cols, i, j, visited):
        visited[i][j] = True
        count = 1 + movingCountCore(threshold, rows, cols, i - 1, j, visited)\
                  + movingCountCore(threshold, rows, cols, i + 1, j, visited)\
                  + movingCountCore(threshold, rows, cols, i, j - 1, visited)\
                  + movingCountCore(threshold, rows, cols, i, j + 1, visited)
    return count


def _movingCountCore(threshold: int, rows: int, cols: int, visited: 'matrix') -> int:
    count = 0
    for i in range(rows):
        for j in range(cols):
            if check(threshold, rows, cols, i, j, visited):
                count += 1
    return count


def check(threshold: int, rows: int, cols: int, 
          row: int, col: int, visited: 'matrix') -> 'bool':
    value = getDigitSum(row) + getDigitSum(col)
    if row >= 0 and row < rows and col >= 0 and col < cols and \
        value <= threshold and not visited[row][col]:
        return True
    return False
    

if __name__ == '__main__':
    threshold = 18
    # print(movingCount(threshold, 10, 10))
    print(_movingCount(threshold, 40, 40))
