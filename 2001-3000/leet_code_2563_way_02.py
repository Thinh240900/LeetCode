from collections import deque


class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()

        def func(target):
            left = 0
            right = len(nums) - 1
            count = 0
            while left < right:
                if nums[left] + nums[right] <= target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count


        a = func(lower-1 )
        b = func(upper)
        return (b - a)


print(Solution().countFairPairs( [0,0,0,0,0,0], 0, 0)) # 15
print(Solution().countFairPairs( [1,7,9,2,5], 11, 11)) # 1
print(Solution().countFairPairs([0,1,7,4,4,5], 3,6)) # 6
