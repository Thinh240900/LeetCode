class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        return res
        # dp = [0] * (len(startTime)*2+1)
        # dp = []
        # index = 0
        # for i in range(len(startTime)):
        #     start = startTime[i]
        #     end = endTime[i]
        #     if start > index:
        #         dp.append(start-index)
        #     dp.append(-1)
        #     index = end
        #
        # return dp

print(Solution().maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5])) # 2
print(Solution().maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10])) # 6
print(Solution().maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5])) # 0