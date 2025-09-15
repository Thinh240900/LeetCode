from collections import Counter


class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        # This solution is copy from LeetCode 2845
        n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res


print(Solution().countInterestingSubarrays([3,2,4] , 2, 1)) # 3
print(Solution().countInterestingSubarrays([3,1,9,6], 3, 0)) # 2