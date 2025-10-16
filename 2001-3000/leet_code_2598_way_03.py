from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        residuals =[0] * value
        for n in nums:
            residuals[n % value] += 1
        minloop = min(residuals)
        ind = residuals.index(minloop)
        return minloop * value + ind

print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 3))
print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5)) # 4
print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7)) # 2