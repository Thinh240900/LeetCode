class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set(nums)
        low = min(s)
        if low < k :
             return -1
        if low > k:
            return len(s)
        return len(s) - 1



print(Solution().minOperations([5,2,4,5,5], 2))  # Output: 2
print(Solution().minOperations([2,1,2], 2)) # -1
print(Solution().minOperations([9,5,7,3], 1))  # Output: 4