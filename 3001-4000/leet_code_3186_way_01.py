from collections import defaultdict, Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        spells = []
        for k in sorted(count.keys()):
            spells.append(k)
        dp = [0] * len(spells)
        current_max = 0
        index_suitable = 0
        for i in range(len(spells)):
            while index_suitable < i and spells[index_suitable] < spells[i] - 2:
                current_max = max(current_max, dp[index_suitable])
                index_suitable += 1
            dp[i] = current_max + count[spells[i]] * spells[i]
        return max(dp)



print(Solution().maximumTotalDamage([1,1,3,4])) # 6
print(Solution().maximumTotalDamage([7,1,6,6])) # 13