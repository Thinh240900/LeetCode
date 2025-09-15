class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        # sort by numerical value in descending order
        vals.sort(key=lambda x: -x[1])
        # select the first k elements and sort them in ascending order by index
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]  # target subsequence
        return res


print(Solution().maxSubsequence(nums = [2,1,3,3], k = 2)) # [3,3]
print(Solution().maxSubsequence(nums = [-1,-2,3,4], k = 3)) # [-1,3,4]
print(Solution().maxSubsequence(nums = [3,4,3,3], k = 2)) # [3,4]