import heapq
from collections import defaultdict
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.task_map = {}

        for uid, tid, p in tasks:
            self.add(uid, tid, p)

    def add(self, userId: int, taskId: int, priority: int):
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        self.task_map[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int):
        uid, p = self.task_map[taskId]
        self.task_map[taskId] = (uid, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, uid))

    def rmv(self, taskId: int):
        del self.task_map[taskId]

    def execTop(self):

        while self.heap:
            p, t, u = heapq.heappop(self.heap)
            taskId = -t
            if taskId in self.task_map and self.task_map[taskId][1] == -p and self.task_map[taskId][0] == u:
                del self.task_map[taskId]
                return u
        return -1


# a = TaskManager([[9,5,0],[0,10,0]])
# a.rmv(10)
# print(a.execTop())




a = TaskManager([[1,101,8],[2,102,20],[3,103,5]])
a.add(4,104,5)
a.edit(102, 9)
print(a.execTop())
a.rmv(101)
a.add(0, 101, 8)
print(a.execTop())



# a = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
# a.add(4, 104, 5)
# a.edit(102, 8)
# print(a.execTop())
# a.rmv(101)
# a.add(5, 105, 15)
# print(a.execTop())
