class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def change(i) :
            return 1 if i == 0 else 0

        start = 0
        count = 0
        while start < len(nums) - 2:
            if nums[start] != 0:
                start += 1
            else:
                count += 1
                nums[start] = change(nums[start])
                nums[start+1] = change(nums[start+1])
                nums[start+2] = change(nums[start+2])
                start += 1
        if 0 in nums:
            return -1
        return count


print(Solution().minOperations([0,1,1,1,0,0]))
print(Solution().minOperations([0,1,1,1,0]))
print(Solution().minOperations([0,1,1,1]))


