class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1].copy()
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # Output: 11