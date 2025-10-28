from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                if left == right:
                    ans += 2
                elif left - right == 1:
                    ans += 1
                elif right - left == 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
        return ans

print(Solution().countValidSelections([1,0,2,0,3]))
print(Solution().countValidSelections([2,3,4,0,4,1,0]))