class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        one = 0
        two = 0
        three = 0
        for num in nums:
            if num == 0:
                one += 1
            elif num == 1:
                two += 1
            else:
                three += 1
        nums[:] = [0] * one + [1] * two + [2] * three




nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)