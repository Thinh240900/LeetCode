class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        index = 0
        while index < len(nums) - 1:
            if nums[index] != nums[index + 1]:
                return False
            index += 2  # skip even numbers
        return True


print(Solution().divideArray([3,2,3,2,2,2]))
print(Solution().divideArray([1,2,3,4]))