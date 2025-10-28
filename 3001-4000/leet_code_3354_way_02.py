from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        nonZeros = sum(1 for x in nums if x != 0)
        n = len(nums)
        for i in range(n):
            if nums[i] == 0 :
                if self.isValid(nums, nonZeros, i, -1):
                    ans += 1
                if self.isValid(nums, nonZeros, i, 1):
                    ans += 1
        return ans

    def isValid(self, nums, nonZeros, start, dir):
        temp = nums[:]
        curr = start
        while nonZeros > 0 and 0 <= curr < len(nums):
            if temp[curr] > 0:
                temp[curr] -= 1
                dir *= -1
                if temp[curr] == 0:
                    nonZeros -= 1
            curr += dir
        return nonZeros == 0

print(Solution().countValidSelections([1,0,2,0,3]))
print(Solution().countValidSelections([2,3,4,0,4,1,0]))