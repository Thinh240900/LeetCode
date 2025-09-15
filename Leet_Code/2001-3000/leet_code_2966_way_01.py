class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        total_arr = n //3
        element_per_arr = n // total_arr
        for i in range(total_arr):
            if nums[i*element_per_arr] + k >= nums[i*element_per_arr+element_per_arr-1]:
                result.append(nums[i*element_per_arr:i*element_per_arr+element_per_arr])
        if len(result) < total_arr:
            return []
        return result


print(Solution().divideArray([1,3,4,8,7,9,3,5,1], 2)) # [[1,1,3],[3,4,5],[7,8,9]]
print(Solution().divideArray([2,4,2,2,5,2], 2)) # []
print(Solution().divideArray([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14)) # [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]