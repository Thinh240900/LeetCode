import bisect
from collections import deque, defaultdict
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []
        dry_days = deque([])
        rain_days = {}

        for i, rain in enumerate(rains):
            if rain:
                if rain in rain_days:
                    for dry in dry_days:
                        if dry > rain_days[rain]:
                            result[dry] = rain
                            dry_days.remove(dry)
                            break
                    else:
                        return []
                rain_days[rain] = i
                result.append(-1)
            else:
                result.append(1)
                dry_days.append(i)

        return result

print(Solution().avoidFlood([1,2,0,0,2,1])) # [-1,-1,2,1,-1,-1]
print(Solution().avoidFlood([1,0,2,0,2,1])) # [-1,1,-1,2,-1,-1]
print(Solution().avoidFlood([1,0,2,3,0,1,2])) # [-1,1,-1,-1,2,-1,-1]
print(Solution().avoidFlood([1,2,3,4])) # [-1,-1,-1,-1]
print(Solution().avoidFlood([1,2,0,1,2])) # []
print(Solution().avoidFlood([0,1,1])) # []