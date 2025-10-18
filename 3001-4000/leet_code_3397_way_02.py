import math
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -math.inf
        cnt = 0

        for num in nums:
            curr = min(max(prev+ 1 , num - k), num + k)
            if curr > prev:
                cnt += 1
                prev = curr




        return cnt

print(Solution().maxDistinctElements( nums = [1,2,2,3,3,4], k = 2)) # 6
print(Solution().maxDistinctElements(nums = [4,4,4,4], k = 1)) # 3