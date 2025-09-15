class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        arr = [[0] * n] + matrix
        arr = [[0] + a for a in arr]
        result = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if arr[i][j] == 1:
                    arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
                    result += arr[i][j]
        return result

print(Solution().countSquares([[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,0,1,0]])) # 13
print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) # 15
print(Solution().countSquares([[1,0,1],[1,1,0],[1,1,0]])) # 7



