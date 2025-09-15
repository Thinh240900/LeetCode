class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1
        for index in range(1, len(nums)):
            if nums[index] <= min_val:
                min_val = nums[index]
            else:
                max_diff = max(max_diff, nums[index] - min_val)
        return max_diff

print(Solution().maximumDifference([7,1,5,4])) # 4
print(Solution().maximumDifference([9,4,3,2])) # -1
print(Solution().maximumDifference([1,5,2,10])) # 9