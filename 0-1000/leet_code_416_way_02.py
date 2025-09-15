class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total =sum(nums)
        if total % 2== 1 :
            return False
        result = int(total / 2)
        length_nums = len(nums)
        dp = {0:0}
        for num in nums:
            for current_sum in list(dp.keys()):
                new_sum = current_sum + num
                if new_sum not in dp :
                    dp[new_sum] = dp[current_sum] + num
                if new_sum == result:
                    return True

        return False
        # def helper(index, current):
        #     if current == result:
        #         return True
        #
        #     if index == length_nums:
        #         return None
        #
        #     with_current = helper(index + 1 , current + nums[index])
        #     if with_current:
        #         return True
        #     return helper(index+1, current)
        #
        # return helper(0,0) or False

print(Solution().canPartition([2,2,2,2,2])) # False
print(Solution().canPartition([1,2,5])) # False
print(Solution().canPartition([14,9,8,4,3,2])) # True
print(Solution().canPartition([1,5,11,5])) # true
print(Solution().canPartition([3,3,3,4,5])) # True
print(Solution().canPartition([1,5,12])) # False
print(Solution().canPartition([1,2,3,5])) #Fasle


