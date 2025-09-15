class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m) :
            for j in range(1, n):
                if matrix[i][j]:
                    temp = min(matrix[i-1][j], matrix[i][j-1])
                    matrix[i][j] = temp + 1 if matrix[i-1][j-1] else temp
        return sum(a for row in matrix for a in row )

print(Solution().countSquares([[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,0,1,0]])) # 13
print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) # 15
print(Solution().countSquares([[1,0,1],[1,1,0],[1,1,0]])) # 7



