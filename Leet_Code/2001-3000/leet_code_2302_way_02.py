class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        l = 0
        s = 0
        for r in range(n):
            s += nums[r]
            while (s * (r - l + 1)) >= k:
                s -= nums[l]
                l += 1
            ans += r - l + 1
        return ans

print(Solution().countSubarrays([2,1,4,3,5], 10)) # 6
print(Solution().countSubarrays([1,1,1,1,1], 10)) # 5
