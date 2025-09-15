import heapq


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 1000000007

        graph = {}
        for i in range(n):
            graph[i] = {}
        for road in roads:
            graph[road[0]][road[1]] = road[2]
            graph[road[1]][road[0]] = road[2]
        shortest_path = {node: float('inf') for node in range(n)}
        shortest_path[0] = 0
        count_path = [0 for _ in range(n)]
        count_path[0] = 1
        pq = [(0, 0)]
        while pq:
            cur_dist, cur_node = heapq.heappop(pq)

            if cur_dist > shortest_path[cur_node]:
                continue

            for neighbor, weight in graph[cur_node].items():
                new_dist = cur_dist + weight
                if new_dist < shortest_path[neighbor]:
                    shortest_path[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
                    count_path[neighbor] =count_path[cur_node]
                elif new_dist == shortest_path[neighbor]:
                    count_path[neighbor] += count_path[cur_node]
        return count_path[n - 1] % MOD


print(Solution().countPaths(12, [[1, 0, 2348], [2, 1, 2852], [2, 0, 5200], [3, 1, 12480], [2, 3, 9628], [4, 3, 7367],
                                 [4, 0, 22195], [5, 4, 5668], [1, 5, 25515], [0, 5, 27863], [6, 5, 836], [6, 0, 28699],
                                 [2, 6, 23499], [6, 3, 13871], [1, 6, 26351], [5, 7, 6229], [2, 7, 28892],
                                 [1, 7, 31744], [3, 7, 19264], [6, 7, 5393], [2, 8, 31998], [8, 7, 3106], [3, 8, 22370],
                                 [8, 4, 15003], [8, 6, 8499], [8, 5, 9335], [8, 9, 5258], [9, 2, 37256], [3, 9, 27628],
                                 [7, 9, 8364], [1, 9, 40108], [9, 5, 14593], [2, 10, 45922], [5, 10, 23259],
                                 [9, 10, 8666], [10, 0, 51122], [10, 3, 36294], [10, 4, 28927], [11, 4, 25190],
                                 [11, 9, 4929], [11, 8, 10187], [11, 6, 18686], [2, 11, 42185], [11, 3, 32557],
                                 [1, 11, 45037]]))  # 166
print(Solution().countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                                [0, 4, 5], [4, 6, 2]]))  # 4
print(Solution().countPaths(2, [[1, 0, 10]]))  # 1
