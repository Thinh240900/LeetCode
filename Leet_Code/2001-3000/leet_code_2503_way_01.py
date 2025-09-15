class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """

        def go_left(i,j,check, value):
            if j - 1 >= 0 and check[i][j-1] == 0 and grid[i][j-1] < value:
                check[i][j-1] = 1
                return 1+start_go(i, j-1, check, value)
            return 0

        def go_up(i,j,check, value):
            if i - 1 >= 0 and check[i-1][j] == 0 and grid[i-1][j] < value:
                check[i-1][j] = 1
                return 1+start_go(i-1, j, check, value)
            return 0

        def go_right(i,j,check, value):
            if j + 1 < len(check[0]) and check[i][j+1] == 0 and grid[i][j+1] < value:
                check[i][j+1] = 1
                return 1+start_go(i, j+1, check, value)
            return 0

        def go_down(i,j,check, value):
            if i + 1 < len(check) and check[i+1][j] == 0 and grid[i+1][j] < value:
                check[i+1][j] = 1
                return 1+start_go(i+1, j, check, value)
            return 0

        def start_go(i,j,check, value):
            count = 0
            count += go_left(i,j,check, value)
            count += go_up(i,j,check, value)
            count += go_right(i,j,check, value)
            count += go_down(i,j,check, value)
            return count

        result = []
        # check = [ [[0] * len(grid[0])] * len(grid)] * len(queries)
        check = [[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(len(queries))]
        for index, value in enumerate(queries):
            if grid[0][0] < value :
                check[index][0][0] = 1
                result.append(1+start_go(0,0,check[index], value))
            else:
                result.append(0)
        return result


# print(Solution().maxPoints([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2]))  # [5, 8, 1]
print(Solution().maxPoints([[5,2,1],[1,1,2]], [3])) # [0]
