class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        result = 0
        for i in range(m):
            for j in range(n):
                mat[i][j] = 0 if mat[i][j] == 0 else mat[i][j-1] + 1
                cur = mat[i][j]
                for k in range(i, -1, -1):
                    cur = min(cur, mat[k][j])
                    if cur == 0:
                        break
                    result += cur
        return result


print(Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]])) # 13
print(Solution().numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])) # 24