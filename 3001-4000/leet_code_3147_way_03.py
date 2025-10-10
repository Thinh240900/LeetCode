from collections import defaultdict
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        n = len(energy)
        for i in range(n-1, -1, -1):
            if i+ k < n:
                dp[i] = energy[i] + dp[i+k]
            else:
                dp[i] = energy[i]

        return max(dp)


print(Solution().maximumEnergy([5,2,-10,-5,1], 3))
print(Solution().maximumEnergy([-2,-3,-1], 2))