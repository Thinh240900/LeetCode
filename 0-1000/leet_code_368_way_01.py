class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        max_len = 0
        max_index = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        return result

print(Solution().largestDivisibleSubset([1, 2, 3, 6, 8]))
print(Solution().largestDivisibleSubset([1, 2, 4, 8]))  # [1, 2, 4, 8]
# print(Solution().largestDivisibleSubset([1, 2, 3]))  # [1, 2]
