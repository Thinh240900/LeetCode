class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings = sorted(meetings)
        result = days
        last = 0
        for start,end in meetings :
            if start <= last:
                if end > last:
                    result -= (end- last )
                else:
                    continue
            else:
                result -= (end - start + 1)
            last = end
        return result




print(Solution().countDays(14, [[6,11],[7,13],[8,9],[5,8],[3,13],[11,13],[1,3],[5,10],[8,13],[3,9]])) # 1
print(Solution().countDays(57, [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]])) # 1
print(Solution().countDays(10, [[5,7],[1,3],[9,10]])) # 2
print(Solution().countDays(5, [[2,4],[1,3]])) # 1
print(Solution().countDays(6, [[1,6]])) # 0