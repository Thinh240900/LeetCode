class Solution(object):
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)

        # If target is not reachable or the transformation is invalid
        if (target + total_sum) % 2 != 0 or target > total_sum or target < -total_sum:
            return 0

        subset_sum = (target + total_sum) // 2

        # Initialize DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum 0: use no numbers

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]
# print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
# print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 5))  # Output: 3
print(Solution().findTargetSumWays([1, 1, 11, 1, 1], 1))  # Output: 0
print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 11))  # Output: 1
print(Solution().findTargetSumWays([1], 1))  # Output: 1
print(Solution().findTargetSumWays([4, 1, 5, 3, 1], 2)) # Output: 3
print(Solution().findTargetSumWays([2, 2, 3], -7))# Output: 1
