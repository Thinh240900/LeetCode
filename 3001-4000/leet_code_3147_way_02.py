from collections import defaultdict
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        best = energy[-1]
        for i in range(k):
            runner = len(energy) - 1 - i
            val = 0
            while runner >= 0:
                here = energy[runner]
                val += here
                best = max(best, val)
                runner -= k
        return best


print(Solution().maximumEnergy([5,2,-10,-5,1], 3))
print(Solution().maximumEnergy([-2,-3,-1], 2))