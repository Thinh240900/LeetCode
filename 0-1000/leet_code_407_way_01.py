import heapq
from collections import defaultdict

class Cell:
    column: int
    row: int
    value: int

    def __init__(self, row: int, column: int, value: int):
        self.column = column
        self.row = row
        self.value = value

    def __lt__(self, other: 'Cell') -> bool:
        return self.value < other.value

    def __eq__(self, other: 'Cell') -> bool:
        return self.row == other.row and self.column == other.column



class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:

        result = 0
        arr_heap = []
        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]

        for col in range(cols):
            heapq.heappush(arr_heap, Cell(0, col, heightMap[0][col]))
            visited[0][col] = True
            heapq.heappush(arr_heap, Cell(rows - 1, col, heightMap[rows - 1][col]))
            visited[rows - 1][col] = True

        for row in range(1, rows - 1):
            heapq.heappush(arr_heap, Cell(row, 0, heightMap[row][0]))
            visited[row][0] = True
            heapq.heappush(arr_heap, Cell(row, cols - 1, heightMap[row][cols - 1]))
            visited[row][cols - 1] = True

        count = 0
        while arr_heap:
            current = heapq.heappop(arr_heap)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = current.row + dx, current.column + dy
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col]:
                    continue
                count += 1
                if heightMap[next_row][next_col] < current.value:
                    result += current.value - heightMap[next_row][next_col]
                    heightMap[next_row][next_col] = current.value
                heapq.heappush(arr_heap, Cell(next_row, next_col, heightMap[next_row][next_col]))
                visited[next_row][next_col] = True


        return result






print(Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))  # 4
print(Solution().trapRainWater([[12,13,1,12],
[13,4,13,12],
[13,8,10,12],
[12,13,12,12],
[13,13,13,13]]

))  # 14
print(Solution().trapRainWater(
    [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))  # 10
