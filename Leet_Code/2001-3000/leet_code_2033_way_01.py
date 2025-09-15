class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        flattened_grid = [item for row in grid for item in row]
        div = flattened_grid[0] % x
        for i in flattened_grid:
            if i % x != div:
                return -1
        sorted_flattened_grid = sorted(flattened_grid)
        middle_item = sorted_flattened_grid[len(flattened_grid)//2]
        count = 0
        for item in flattened_grid:
            count += abs(item - middle_item) // x
        return count

print(Solution().minOperations([[2,4],[6,8]], 2)) # 4
print(Solution().minOperations([[1,5],[2,3]], 1)) # 5
print(Solution().minOperations([[1,2],[3,4]], 2)) # -1

