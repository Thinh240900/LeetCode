from collections import defaultdict


class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = set(nums)
        left = 0
        right = 0
        count = 0
        while right < len(nums):
            if set(nums[left:right + 1]) == distinct_nums:
                count += len(nums) - right
                left += 1
                if left > right:
                    right = left
            else:
                right += 1

        return count


print(Solution().countCompleteSubarrays([5,5,5,5])) # 10
print(Solution().countCompleteSubarrays([1,3,1,2,2])) # 4
