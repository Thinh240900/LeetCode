import math
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -math.inf
        cnt = 0

        for num in nums:
            if prev < num - k:
                cnt += 1
                prev = num - k
            elif prev < num + k:
                prev += 1
                cnt += 1




        return cnt

print(Solution().maxDistinctElements( nums = [1,2,2,3,3,4], k = 2)) # 6
print(Solution().maxDistinctElements(nums = [4,4,4,4], k = 1)) # 3