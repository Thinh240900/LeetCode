class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        largest = nums[0]
        largest_diff = largest - nums[1]
        result = 0

        for i in range(len_nums-2):
            largest = max(largest, nums[i])
            largest_diff = max(largest_diff, largest - nums[i+1])
            result = max(result, largest_diff * nums[i+2])
        return result



print(Solution().maximumTripletValue([12,6,1,2,7]))
print(Solution().maximumTripletValue([1,10,3,4,19]))
print(Solution().maximumTripletValue([1,2,3]))