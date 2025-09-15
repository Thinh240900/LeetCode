from sortedcontainers import SortedList


class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid):
            p = pills
            # Ordered set of workers
            ws = SortedList(workers[m - mid:])
            # Enumerate each task from largest to smallest
            for i in range(mid - 1, -1, -1):
                # If the largest element in the ordered set is greater than or equal to tasks[i]
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

print(Solution().maxTaskAssign([5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5)) # 3
print(Solution().maxTaskAssign([3,2,1], workers = [0,3,3], pills = 1, strength = 1)) # 3
print(Solution().maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5)) # 1
print(Solution().maxTaskAssign([10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10)) # 2
# custom test case
print(Solution().maxTaskAssign([10,19], workers = [10, 0], pills = 2, strength = 10)) # 2
print(Solution().maxTaskAssign([11,19], workers = [10, 0], pills = 1, strength = 10)) # 1
