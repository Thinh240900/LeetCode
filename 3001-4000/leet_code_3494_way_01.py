from typing import List


class Solution:
    def minTime(self, skills: List[int], manas: List[int]) -> int:
        n = len(skills)
        m = len(manas)
        done = [0] * n
        done[0] = skills[0] * manas[0]

        for i in range(1, n):
            done[i] += done[i-1] + skills[i] * manas[0]

        for i in range(1, m):
            done[0] += skills[0] * manas[i]
            for j in range(1, n):
                done[j] = max(done[j], done[j-1]) + skills[j] * manas[i]
            for j in range(n-1, 0, -1):
                done[j-1] = done[j] - skills[j] * manas[i]

        return done[n-1]


print(Solution().minTime(skills = [5,4], manas = [3,2,6,1])) # 85
print(Solution().minTime(skills = [1,5,2,4], manas = [5,1,4,2])) # 110
print(Solution().minTime(skills = [1,1,1], manas = [1,1,1])) # 5
print(Solution().minTime(skills = [1,2,3,4], manas = [1,2])) # 21