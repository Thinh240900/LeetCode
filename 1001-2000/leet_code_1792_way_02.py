import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        classes = [
            (-(1-p/t) / (t +1), p , t)
            for p, t in classes
        ]
        heapq.heapify(classes)
        for _ in range(extraStudents):
            _ , p , t = heapq.heappop(classes)
            p += 1
            t += 1
            heapq.heappush(classes, (-(1-p/t) / (t +1), p , t))
        total = 0.0
        for _,p, t in classes:
            total += p / t

        return total / len(classes)

print(Solution().maxAverageRatio([[97,500],[30,915],[400,856],[444,623],[781,786],[3,713]], 8)) # 0.40288
print(Solution().maxAverageRatio([[583,868],[783,822],[65,262],[121,508],[461,780],[484,668]], 8)) # 0.57472
print(Solution().maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4)) # 0.53485
print(Solution().maxAverageRatio([[1,2],[3,5],[2,2]], 2)) # 0.7833


### 3,5 3,9 4,5 2,10 -> 0,1
###