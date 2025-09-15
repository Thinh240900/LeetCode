class Solution:
    def numberOfWays(self, n, x):
        """
       :type n: int
       :type x: int
       :rtype: int
       """
        MOD = 10**9 + 7
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1) :
            val = i ** x
            for j in range(n+1):
                dp[i][j] = dp[i-1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-val]) % MOD

        return dp[n][n]


print(Solution().numberOfWays(4, 1))  # 2
print(Solution().numberOfWays(10, 2))  # 1
