class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]  # Update the last element of the current row with the value of the last element of the previous row.
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j - 1]) + triangle[i][j]
            dp[i][0] = dp[i-1][0] + triangle[i][0]  # Update the first element of the current row with the sum of the first element and the first element of the previous row.

        return min(dp[-1])


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # Output: 11