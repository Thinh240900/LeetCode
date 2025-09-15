class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        dp = [0] * (n + 1)
        dp[0] = 1.0
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if 0 <= i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])


print(Solution().new21Game(n = 10, k = 1, maxPts = 10)) # 1
print(Solution().new21Game(n = 6, k = 1, maxPts = 10)) # 0.6
print(Solution().new21Game(n = 21, k = 17, maxPts = 10)) # 0.73278