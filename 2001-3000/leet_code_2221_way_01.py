from math import comb
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1) :
            for j in range(n-i-1):
                nums[j] =( nums[j] + nums[j+1]) % 10
        return nums[0]


print(Solution().triangularSum([1,2,3,4,5])) # 8
print(Solution().triangularSum([5])) # 5