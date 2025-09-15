class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        delta = [0] * (len(nums)+1)
        for left, right in queries:
            delta[left] -=1
            delta[right+1] +=1
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += delta[i]
            nums[i] += prefix_sum
        if all(num <= 0 for num in nums):
            return True
        return False
print(Solution().isZeroArray(nums = [1,0,1], queries = [[0,2]])) # true
print(Solution().isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]])) # false