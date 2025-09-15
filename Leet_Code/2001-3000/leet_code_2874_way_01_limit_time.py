class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        prefix_max = [0] * (len_nums)
        suffix_max = [0] * (len_nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums-1):
                prefix_max[j] = max(prefix_max[j], nums[i])
            for j in range(1, i):
                suffix_max[j] = max(suffix_max[j], nums[i])
        result = 0
        for j in range(1, len_nums-1):
            result = max(result, (prefix_max[j] - nums[j]) * suffix_max[j])
        return result



print(Solution().maximumTripletValue([12,6,1,2,7]))
print(Solution().maximumTripletValue([1,10,3,4,19]))
print(Solution().maximumTripletValue([1,2,3]))