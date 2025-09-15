class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            min_index = 0
            for j in range(1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[min_index] *= multiplier
        return nums