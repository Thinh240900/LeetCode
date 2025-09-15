from collections import defaultdict


class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [1] + [0] * (n -1)
        share = 0 # current share of people who know the secret
        for i in range(1, n):
            dp[i] = share = share + dp[i-delay] - dp[i-forget]


        return sum(dp[-forget:]) % MOD




print(Solution().peopleAwareOfSecret( n = 6, delay = 1, forget = 2)) # 2
print(Solution().peopleAwareOfSecret( n = 6, delay = 2, forget = 4)) # 5
print(Solution().peopleAwareOfSecret(n = 4, delay = 1, forget = 3)) # 6