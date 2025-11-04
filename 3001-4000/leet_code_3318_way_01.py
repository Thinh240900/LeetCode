from collections import defaultdict, Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            cnt = Counter(nums[i: i+ k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key*value for key, value in freq[:x])
            ans.append(xsum)
        return ans


print(Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)) # [6,10,12]
print(Solution().findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2)) # [11,15,15,15,12]
