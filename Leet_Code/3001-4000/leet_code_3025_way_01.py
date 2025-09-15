class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: (-x[0], x[1]))
        result = 0
        for i in range(len(points) - 1):
            y = 1 << 31
            for j in range(i + 1, len(points)):
                if points[i][1] <= points[j][1] < y:
                    result = result + 1
                    y = points[j][1]

        return result


print(Solution().numberOfPairs([[0, 1], [1, 3], [6, 1]]))  # 2
print(Solution().numberOfPairs([[0, 5], [4, 5]]))  # 1
print(Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]]))  # 0
print(Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]]))  # 2
print(Solution().numberOfPairs([[1, 3], [3, 1], [1, 1]]))  # 2
