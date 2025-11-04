from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        prev_max = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                time += min(neededTime[i], prev_max)
                prev_max = max(prev_max, neededTime[i])
            else:
                prev_max = neededTime[i]
        return time

print(Solution().minCost("aabaa", [1,2,3,4,1])) # 2
print(Solution().minCost("abaac", [1,2,3,4,1])) # 3
print(Solution().minCost("abc", [1,2,3])) # 0
