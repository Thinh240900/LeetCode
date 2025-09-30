from math import comb
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            result = (result + comb(n - 1, i) * nums[i]) % 10

        return result

print(Solution().triangularSum([1,2,3,4,5])) # 8
print(Solution().triangularSum([5])) # 5