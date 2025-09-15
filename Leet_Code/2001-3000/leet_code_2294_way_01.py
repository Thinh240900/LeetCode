class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 1
        min_num_in_subarray = nums[0]
        for num in nums:
            if num - min_num_in_subarray > k :
                ans +=1
                min_num_in_subarray = num
        return ans

print(Solution().partitionArray([3,6,1,2,5], 2)) # 2
print(Solution().partitionArray([1,2,3], 1)) # 2
print(Solution().partitionArray([2,2,4,5], 0)) # 3