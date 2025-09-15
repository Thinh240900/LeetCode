from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency_map = Counter(nums)
        ans = 0

        for num in frequency_map:
            if num + 1 in frequency_map:
                ans = max(ans, frequency_map[num] + frequency_map[num + 1])
        return ans


print(Solution().findLHS([1,3,2,2,5,2,3,7])) # 5
print(Solution().findLHS([1,1,1,1])) # 0
print(Solution().findLHS([1,2,3,4])) # 2
