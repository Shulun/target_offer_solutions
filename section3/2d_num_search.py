# -*- coding:utf-8 -*-

class Solution:
    def find(self, array, target):
        if not array:
            return False
        if not isinstance(target, (int, float)):
            return False
        row_num = len(array)
        col_num = len(array[0])

        i = 0 # row
        j = col_num - 1 # column

        while i < row_num and j >= 0:
            if target < array[i][j]:
                j -= 1
            elif target > array[i][j]:
                i += 1
            else:
                return True
        return False

    # Output the number of target in the matrix
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        count = 0
        while row < rows and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                count += 1
                col -= 1
        return count

if  __name__ == '__main__':
    array = [
                [1, 2, 8, 9],
                [2, 4, 9, 12],
                [4, 7, 10, 13],
                [6, 8, 11, 15]
            ]
    array2 = []
    array3 = [['a', 'b', 'c'],
            ['b', 'c', 'd']]
    array4 = [
                [62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
                [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
                [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
                [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
                [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
                [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]
            ]


    findtarget = Solution()
    print(findtarget.find(array, 10))
    print(findtarget.find(array, 30))
    print(findtarget.find(array, 13.0))
    print(findtarget.find(array, ''))
    print(findtarget.find(array2, 10))
    print(findtarget.find(array3, 'b'))
    print(findtarget.searchMatrix(array4, 81))
    print(findtarget.searchMatrix(array4, 85))
