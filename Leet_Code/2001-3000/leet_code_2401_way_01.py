class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        used_bits = 0
        window_start = 0
        max_length = 0

        for window_end in range(len(nums)):
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[window_start]
                window_start += 1
            used_bits |= nums[window_end]
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

print(Solution().longestNiceSubarray([1,3,8,48,10]))
print(Solution().longestNiceSubarray([3,1,5,11,13]))