class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if any(num < k for num in nums):
            return -1
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                if num != k:
                    dict[num] = 1
        return len(dict)



print(Solution().minOperations([5,2,4,5,5], 2))  # Output: 2
print(Solution().minOperations([2,1,2], 2)) # -1
print(Solution().minOperations([9,5,7,3], 1))  # Output: 4