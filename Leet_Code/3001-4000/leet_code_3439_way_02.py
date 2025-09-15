class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        dp = []
        index = 0
        for i in range(len(startTime)):
            start = startTime[i]
            end = endTime[i]
            if start > index:
                dp.append(start-index)
            dp.append(0)
            index = end
        dp.append(eventTime - endTime[-1])
        res = 0
        for i in range()

        return dp

print(Solution().maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5])) # 2
print(Solution().maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10])) # 6
print(Solution().maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])) # 0