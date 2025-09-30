from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        count = 0

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                temp = values[i] * values[j]
                count += j - i - 1
                dp[i][j] = min(dp[i][k] + dp[k][j] + temp * values[k] for k in range(i+1,j))

        print("count " + str(count))
        return dp[0][n-1]

print(Solution().minScoreTriangulation([1,2,3])) # 6
print(Solution().minScoreTriangulation([3,7,4,5])) # 144
print(Solution().minScoreTriangulation([1,3,1,4,1,5])) # 13
print(Solution().minScoreTriangulation([1,3,1,4,1,5,2,5,2,5,3]))