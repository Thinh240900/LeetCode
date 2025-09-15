import heapq


class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        queries.sort(key=lambda x: x[0] or -x[1])
        heap = []
        delta = [0] * (len(nums) + 1)
        prefix_sum = 0
        j = 0
        for i, num in enumerate(nums):
            prefix_sum += delta[i]
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(heap, -queries[j][1])
                j += 1
            while heap and prefix_sum < num and -heap[0] >=i:
                prefix_sum += 1
                delta[-heapq.heappop(heap) + 1 ] -= 1
            if prefix_sum < num:
                return -1
        return len(heap)


print(Solution().maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]])) # 1
print(Solution().maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]])) # 2
print(Solution().maxRemoval(nums = [0,0,1,1,0,0], queries = [[2,3],[0,2],[3,5]])) # 2
print(Solution().maxRemoval(nums = [1,2,3,4], queries = [[0,3]])) # -1