class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        result = 0
        last = 0
        for start, end in meetings:
            if start > last :
                result += (start - last - 1)
            last = max(last,end)
        result += days - last


        return result




print(Solution().countDays(8, [[3,4],[4,8],[2,5],[3,8]])) # 1
print(Solution().countDays(14, [[6,11],[7,13],[8,9],[5,8],[3,13],[11,13],[1,3],[5,10],[8,13],[3,9]])) # 1
print(Solution().countDays(57, [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]])) # 1
print(Solution().countDays(10, [[5,7],[1,3],[9,10]])) # 2
print(Solution().countDays(5, [[2,4],[1,3]])) # 1
print(Solution().countDays(6, [[1,6]])) # 0