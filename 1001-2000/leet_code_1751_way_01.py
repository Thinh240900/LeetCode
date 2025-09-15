import bisect


class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort()
        n= len(events)
        start = [ event[0] for event in events]
        dp = [[-1]* n for _ in range(k+1)]

        def dfs(cur_index, count) :
            if count ==0 or cur_index==n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]
            next_index = bisect.bisect_right(start, events[cur_index][1])
            dp[count][cur_index] = max(dfs(cur_index+1, count), events[cur_index][2] + dfs(next_index, count-1))
            return dp[count][cur_index]
        return dfs(0, k)


print(Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2)) # 7
print(Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2)) # 10
print(Solution().maxValue(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3)) # 9