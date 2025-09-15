class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0

        for start in range(len(nums) -2 ):
            if nums[start] == 0:
                count += 1
                nums[start] = nums[start] ^ 1
                nums[start+1] = nums[start+1] ^ 1
                nums[start+2] = nums[start+2] ^ 1


        if 0 in nums:
            return -1

        return count


print(Solution().minOperations([0,1,1,1,0,0]))
print(Solution().minOperations([0,1,1,1,0]))
print(Solution().minOperations([0,1,1,1]))