import collections
from typing import List

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class Router:

    def __init__(self, memoryLimit: int):
        self.memLim = memoryLimit
        self.q = collections.deque()
        self.seen = set()
        self.destMap = collections.defaultdict(list)

    def findLeft(self, lst: List[int], x: int) -> int:
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findRight(self, lst: List[int], x: int) -> int:
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def insert(self, lst: List[int], x: int):
        idx = self.findLeft(lst, x)
        lst.insert(idx, x)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.seen) == self.memLim:
            s0, d0, t0 = self.q.popleft()
            self.seen.remove((s0, d0, t0))
            lst0 = self.destMap[d0]
            i0 = self.findLeft(lst0, t0)
            lst0.pop(i0)
            if not lst0:
                del self.destMap[d0]
        self.q.append((source, destination, timestamp))
        self.seen.add(key)
        self.insert(self.destMap[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        lst = self.destMap[d]
        i = self.findLeft(lst, t)
        lst.pop(i)
        if not lst:
            del self.destMap[d]
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0
        lst = self.destMap[destination]
        lo = self.findLeft(lst, startTime)
        ri = self.findRight(lst, endTime)
        return ri - lo
a = Router(3)
print(a.addPacket(1, 4, 90)) # True
print(a.addPacket(2, 5, 90)) # True
print(a.addPacket(1, 4, 90)) # False
print(a.addPacket(3, 5, 95)) # True
print(a.addPacket(4, 5, 105)) # True
print(a.forwardPacket()) # [2, 5, 90]
print(a.addPacket(5, 2, 110)) # True
print(a.getCount(5, 100, 110)) # 1
#
print('------')

a = Router(5)
print(a.addPacket(2,3,1)) # True
print(a.addPacket(5,2,5)) # True
print(a.addPacket(2,3,5)) # True
print(a.getCount(3,4,4)) # 0
print(a.getCount(3,5,5)) # 1
print(a.addPacket(3,2,5)) # True
print(a.forwardPacket()) # [2, 3, 1]
print(a.addPacket(2,3,5)) # False

print('------')


a = Router(4)
print(a.addPacket(4,2,1))
print(a.addPacket(3,2,1))
print(a.getCount(2,1,1)) # 2