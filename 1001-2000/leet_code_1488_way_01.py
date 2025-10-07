import bisect
from collections import deque, defaultdict
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []
        dry_days = []
        rain_days = {}


        for i, rain in enumerate(rains):
            if rain > 0 :
                if rain_days.get(rain, -1) == -1:
                    rain_days[rain] = i
                else:
                    if len(dry_days):
                        index = bisect.bisect_right(dry_days, rain_days[rain])
                        if index == len(dry_days):
                            return []
                        else:
                            result[dry_days[index]] = rain
                            rain_days[rain] = i
                            dry_days.pop(index)
                    else:
                        return []
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