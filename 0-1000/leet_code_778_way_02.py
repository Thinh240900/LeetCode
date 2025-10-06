import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        highest = grid[0][0]
        directions = [-1, 0, 1, 0, -1]
        while heap:
            height, i, j = heapq.heappop(heap)
            visited[i][j] = True
            if height > highest:
                highest = height
            if i == n - 1 and j == n - 1:
                return highest
            for index in range(4):
                nx, ny = i + directions[index], j + directions[index+1]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))

print(Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])) # 16
print(Solution().swimInWater([[0,2],[1,3]])) # 3
