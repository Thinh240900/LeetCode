from collections import defaultdict, Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)
        strengths = {k: k * v for k, v in counter.items()}
        spells = [0, 0, 0] + sorted(list(strengths.keys()))
        dp = [0] * len(spells)
        for i in range(3, len(spells)):
            if spells[i] - spells[i-1] > 2 :
                dp[i] = dp[i-1] + strengths[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strengths[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strengths[spells[i]])

        return dp[-1]



print(Solution().maximumTotalDamage([1,1,3,4])) # 6
print(Solution().maximumTotalDamage([7,1,6,6])) # 13
