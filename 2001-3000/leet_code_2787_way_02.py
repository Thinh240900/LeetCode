class Solution:
    def numberOfWays(self, n, x):
        """
       :type n: int
       :type x: int
       :rtype: int
       """
        MOD = 10**9 + 7
        stack = []
        for i in range(1, n+1):
            if i**x <= n:
                stack.append(i**x)
            else:
                break

        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for power in stack:
            for i in range(n, power-1, -1):
                dp[i] = (dp[i] + dp[i-power]) % MOD
        return dp[n]



print(Solution().numberOfWays(4, 1))  # 2
print(Solution().numberOfWays(10, 2))  # 1
