from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        alantic = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, visited):
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, alantic)
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, alantic)


        return list(pacific & alantic)

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) #[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(Solution().pacificAtlantic([[1]])) # [[0,0]]
