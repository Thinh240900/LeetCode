from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        result = [0] * n
        potions.sort()

        def findRight(left, right, spell, target):
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1
            return left


        for i in range(n)  :
            result[i] = m - findRight(0, m, spells[i], success)
        return result


print(Solution().successfulPairs( spells = [5,1,3], potions = [1,2,3,4,5], success = 7)) # [4,0,3]
print(Solution().successfulPairs( spells = [3,1,2], potions = [8,5,8], success = 16)) # [2,0,2]
