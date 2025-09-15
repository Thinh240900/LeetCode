from collections import defaultdict


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        set_row = set()
        set_col = set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    set_row.add(row)
                    set_col.add(col)

        for row in range(m):
            for col in range(n):
                if row in set_row or col in set_col:
                    matrix[row][col] = 0
        return None



matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
print(matrix)
