class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new_arr = sorted(nums, reverse=True)[:k]
        ans = []
        for num in nums:
            if num in new_arr:
                ans.append(num)
                new_arr.remove(num)
        return ans


print(Solution().maxSubsequence(nums = [2,1,3,3], k = 2)) # [3,3]
print(Solution().maxSubsequence(nums = [-1,-2,3,4], k = 3)) # [-1,3,4]
print(Solution().maxSubsequence(nums = [3,4,3,3], k = 2)) # [3,4]