class Solution:
    def countGoodStrings(self, low, high, zero, one) :
        # Use dp[i] to record to number of good strings of length i.
        dp = [1] + [-1] * (high)
        mod = 10 ** 9 + 7

        # Find the number of good strings of length `end`.
        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]

        # Add up the number of strings with each valid length [low ~ high].
        return sum(dfs(end) for end in range(low, high + 1)) % mod

print(Solution().countGoodStrings(3, 3, 1, 1))
print(Solution().countGoodStrings(2, 3, 1, 2))
print(Solution().countGoodStrings(10, 10, 2, 1))
