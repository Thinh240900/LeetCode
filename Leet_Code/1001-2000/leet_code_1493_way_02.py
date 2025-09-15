class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = current = previous = 0
        for num in nums:
            if num:
                current += 1
                result = max(result, previous + current)
            else:
                previous = current
                current = 0
        return result - (result == len(nums))

print(Solution().longestSubarray([1,1,0,1])) # 3
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
print(Solution().longestSubarray([1,1,1])) # 2
print(Solution().longestSubarray([1])) # 0
print(Solution().longestSubarray([0])) # 0
print(Solution().longestSubarray([0, 1, 0])) # 1
