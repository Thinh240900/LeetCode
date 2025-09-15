class Solution:
    def findTargetSumWays(self, nums, target) :
        total_sum = sum(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # Initialize the first row of the DP table
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] = 1

        # Fill the DP table
        for index in range(1, len(nums)):
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[index - 1][sum_val + total_sum] > 0:
                    dp[index][sum_val + nums[index] + total_sum] += dp[index - 1][sum_val + total_sum]
                    dp[index][sum_val - nums[index] + total_sum] += dp[index - 1][sum_val + total_sum]

        # Return the result if the target is within the valid range
        return (
            0
            if abs(target) > total_sum
            else dp[len(nums) - 1][target + total_sum]
        )


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 5))  # Output: 3
print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 11))  # Output: 1
print(Solution().findTargetSumWays([1], 1))  # Output: 1
print(Solution().findTargetSumWays([4, 1, 5, 3, 1], 2)) # Output: 3
print(Solution().findTargetSumWays([2, 2, 3], -7))# Output: 1
