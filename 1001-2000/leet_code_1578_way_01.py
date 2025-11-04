from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = 0
        ans = 0
        current = [neededTime[0]]
        max_time = [neededTime[0]]
        count_par = 0
        for right in range(1, len(colors)):
            if colors[right] == colors[left]:
                current[count_par] += neededTime[right]
                max_time[count_par] = max(max_time[count_par], neededTime[right])
            else:
                left = right
                count_par += 1
                current.append(neededTime[right])
                max_time.append(neededTime[right])
        for cur_total, cur_max in zip(current, max_time):
            ans += cur_total - cur_max
        return ans

print(Solution().minCost("aabaa", [1,2,3,4,1])) # 2
print(Solution().minCost("abaac", [1,2,3,4,1])) # 3
print(Solution().minCost("abc", [1,2,3])) # 0
