import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        arr = []

        for item in classes:
             if item[0] != item[1]:
                 arr.append((
                         -(
                                 (item[0]+1) / (item[1]+1) - (item[0]) / (item[1])
                         )
                 ,[item[0], item[1]]))
        heapq.heapify(arr)

        while extraStudents > 0 and len(arr) > 0:
            _, current = heapq.heappop(arr)
            heapq.heappush(arr, (
                -(
                        (current[0] + 2) / (current[1] + 2) -        (current[0] +1) / (current[1] +1)
                )
                ,[current[0] + 1, current[1]+1]))
            extraStudents -= 1
        n = len(classes)
        m = len(arr)
        total = sum(item[0] / item[1] for _, item in arr) + (n - m)
        return total / max(m, n)

print(Solution().maxAverageRatio([[97,500],[30,915],[400,856],[444,623],[781,786],[3,713]], 8)) # 0.40288
print(Solution().maxAverageRatio([[583,868],[783,822],[65,262],[121,508],[461,780],[484,668]], 8)) # 0.57472
print(Solution().maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4)) # 0.53485
print(Solution().maxAverageRatio([[1,2],[3,5],[2,2]], 2)) # 0.7833


### 3,5 3,9 4,5 2,10 -> 0,1
###