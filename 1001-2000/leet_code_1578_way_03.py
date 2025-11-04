from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        current = 0
        allTime = 0
        while (current + 1 < len(colors)):
            if colors[current] == colors[current + 1]:
                max_partition = neededTime[current]

                while current + 1 < len(colors) and colors[current] == colors[current + 1]:
                    current += 1
                    if neededTime[current] > max_partition:
                        allTime += max_partition
                        max_partition = neededTime[current]
                    else:
                        allTime += neededTime[current]
            current += 1
        return allTime

print(Solution().minCost("aabaa", [1,2,3,4,1])) # 2
print(Solution().minCost("abaac", [1,2,3,4,1])) # 3
print(Solution().minCost("abc", [1,2,3])) # 0
