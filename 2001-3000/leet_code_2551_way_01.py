import heapq


class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        if k == len(weights) or k == 1:
            return 0
        pq_min = []
        pq_max = []
        for i in range(len(weights)-1):
            heapq.heappush(pq_min, (weights[i] + weights[i+1], i))
            heapq.heappush(pq_max, (-(weights[i] + weights[i+1]), i))

        min_total = 0
        max_total = 0
        for i in range(k-1):
            min_total += heapq.heappop(pq_min)[0]
            max_total -= heapq.heappop(pq_max)[0]

        return max_total-min_total



print(Solution().putMarbles([1,3,5,1] , 2))
print(Solution().putMarbles([1,3] , 2))