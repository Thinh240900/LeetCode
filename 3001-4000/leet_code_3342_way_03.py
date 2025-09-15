import heapq


class Solution:
    def minTimeToReach(self, moveTime):
        row = len(moveTime)
        col = len(moveTime[0])
        visited = [[False] * col for _ in range(row)]
        q = [(0,0,0,0)]
        heapq.heapify(q)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            curr_time, x, y, pass_count = heapq.heappop(q)
            if x == row-1 and y == col-1:
                return curr_time
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    time_move =  1 if pass_count % 2 == 0 else 2
                    if curr_time >= moveTime[nx][ny] :
                        heapq.heappush(q, (curr_time+time_move, nx, ny, pass_count+1))
                    else:
                        heapq.heappush(q, (moveTime[nx][ny] + time_move, nx, ny, pass_count+1))
        return -1

print(Solution().minTimeToReach([[0,3, 2],[0,4,1]])) # 7


print(Solution().minTimeToReach([[0,0,0,0],[0,0,0,0]])) # 6
print(Solution().minTimeToReach([[0,58],[27,69]])) # 71
print(Solution().minTimeToReach([[0,4],[4,4]])) # 7
print(Solution().minTimeToReach([[0,1],[1,2]])) # 4