class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        left_most = cols - 1
        right_most = 0
        top_most = rows -1
        bottom_most = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    left_most = min(left_most, j)
                    right_most = max(right_most, j)
                    top_most = min(top_most, i)
                    bottom_most = max(bottom_most, i)
        return (right_most - left_most + 1) * (bottom_most - top_most + 1)

print(Solution().minimumArea([[1,0],[0,0]])) # 1
print(Solution().minimumArea([[0,1,0],[1,0,1]])) # 6
