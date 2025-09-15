from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumber = set()
        for num in nums:
            if num > 0:
                positiveNumber.add(num)
        if len(positiveNumber) > 0:
            return sum(positiveNumber)
        return max(nums)


print(Solution().maxSum([1,2,3,4,5]))
print(Solution().maxSum([1,1,0,1,1]))
print(Solution().maxSum([1,2,-1,-2,1,0,-1]))