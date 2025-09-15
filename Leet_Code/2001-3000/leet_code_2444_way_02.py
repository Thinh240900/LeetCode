from collections import defaultdict


class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """

        minK_index = -1
        maxK_index = -1
        count = 0
        over_index = -1
        for i in range(len(nums)):
            if nums[i] <= minK:
                if nums[i] == minK:
                    minK_index = i
                else :
                    over_index = i
            if nums[i] >= maxK:
                if nums[i] == maxK:
                    maxK_index = i
                else:
                    over_index = i

            if minK_index > over_index and maxK_index > over_index:
                count += min(minK_index, maxK_index) - over_index

        return count

print(Solution().countSubarrays([1,2,1,3,5,2,7,5], 1, 5)) # 6
print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5)) # 2
print(Solution().countSubarrays([1,1,1,1], 1, 1)) # 10