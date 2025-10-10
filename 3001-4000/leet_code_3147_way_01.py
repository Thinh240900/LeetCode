from collections import defaultdict
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        check = defaultdict(int)
        result = -1001

        for i in range(len(energy)-1, -1, -1):
            check[i%k] += energy[i]
            result = max(result, check[i%k])
        return result



print(Solution().maximumEnergy([5,2,-10,-5,1], 3))
print(Solution().maximumEnergy([-2,-3,-1], 2))