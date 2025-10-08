import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        result = []
        potions.sort()

        for spell in spells:
            compare = (spell + success - 1 ) // spell
            result.append(m - bisect.bisect_left(potions, compare))
        return result


print(Solution().successfulPairs( spells = [5,1,3], potions = [1,2,3,4,5], success = 7)) # [4,0,3]
print(Solution().successfulPairs( spells = [3,1,2], potions = [8,5,8], success = 16)) # [2,0,2]
