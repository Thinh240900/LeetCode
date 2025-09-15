import heapq
from collections import defaultdict


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        max_day = max(event[1] for event in events)
        n = len(events)
        ans, j = 0, 0
        pq = []
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans +=1
        return ans

print(Solution().maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])) # 5
print(Solution().maxEvents([[1,2],[2,3],[3,4]])) # 3
print(Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]])) # 4
print(Solution().maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])) # 5
