from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for start in range(n-3, -1, -1):
            for end in range(start+2,n):
                dp[start][end] = float('inf')
                temp = values[start] * values[end]
                for k in range(start+1, end):
                    count += 1
                    dp[start][end] = min(dp[start][end], dp[start][k] + dp[k][end] + temp * values[k] )


        print("count: ", count)
        return dp[0][n-1]


print(Solution().minScoreTriangulation([1,2,3])) # 6
print(Solution().minScoreTriangulation([3,7,4,5])) # 144
print(Solution().minScoreTriangulation([1,3,1,4,1,5])) # 13
print(Solution().minScoreTriangulation([1,3,1,4,1,5,2,5,2,5,3]))
