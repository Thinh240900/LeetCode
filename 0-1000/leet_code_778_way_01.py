import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        highest = grid[0][0]
        while heap:
            height, i, j = heapq.heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j] = True
            if height > highest:
                highest = height
            if i == n - 1 and j == n - 1:
                return highest
            if i >0:
                heapq.heappush(heap, (grid[i - 1][j], i - 1, j))
            if j < n - 1:
                heapq.heappush(heap, (grid[i][j + 1], i, j + 1))
            if j > 0:
                heapq.heappush(heap, (grid[i][j - 1], i, j - 1))
            if i < n - 1:
                heapq.heappush(heap, (grid[i + 1][j], i + 1, j))

print(Solution().swimInWater([[0,2],[1,3]])) # 3
print(Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])) # 16
