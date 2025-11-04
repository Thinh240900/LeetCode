from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        last_ch = ''
        last_time = 0
        for ch, time in zip(colors, neededTime):
            if ch == last_ch:
                if time > last_time:
                    total += last_time
                    last_time = time
                else:
                    total += time
            else:
                last_ch = ch
                last_time = time
        return total


print(Solution().minCost("aabaa", [1,2,3,4,1])) # 2
print(Solution().minCost("abaac", [1,2,3,4,1])) # 3
print(Solution().minCost("abc", [1,2,3])) # 0
