import heapq
from collections import defaultdict


class Solution(object):
    def maxRemoval(self, nums, queries):
        n = len(nums)
        dic = defaultdict(list)
        for l, r in queries:
            dic[l].append(r)

        query_increments = [0 for _ in range(n + 1)]
        cumu_incr = 0
        heap = []  # max-heap
        for i, num in enumerate(nums):
            cumu_incr += query_increments[i]
            for r in dic[i]:
                heapq.heappush(heap, -r)

            while cumu_incr < num:
                if not heap or -heap[0] < i:
                    return -1

                r = -heapq.heappop(heap)
                cumu_incr += 1
                query_increments[r + 1] -= 1

        return len(heap)


print(Solution().maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]])) # 1
print(Solution().maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]])) # 2
print(Solution().maxRemoval(nums = [0,0,1,1,0,0], queries = [[2,3],[0,2],[3,5]])) # 2
print(Solution().maxRemoval(nums = [1,2,3,4], queries = [[0,3]])) # -1