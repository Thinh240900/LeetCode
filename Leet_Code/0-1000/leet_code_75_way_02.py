class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for start in range(n):
            if nums[start] == 0:
                continue
            for end in range(n-1, start, -1):
                if nums[end] == 2:
                    continue
                if nums[start] != 0 and nums[end] != 2:
                    nums[start], nums[end] = nums[end], nums[start]





nums = [2,0,1]
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)