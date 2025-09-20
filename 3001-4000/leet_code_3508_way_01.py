import bisect
import heapq
from collections import defaultdict, deque


class Packet:
    def __init__(self, source: int, destination: int, timestampL: int):
        self.source = source
        self.destination = destination
        self.timestampL = timestampL

    def __eq__(self, other):
        return self.source == other.source and self.destination == other.destination and self.timestampL == other.timestampL

    def __lt__(self, other):
        return self.timestampL < other.timestampL

    def __iter__(self):
        yield self.source
        yield self.destination
        yield self.timestampL

    def tolist(self) -> list[int]:
        return [self.source, self.destination, self.timestampL]

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.storage = deque()
        self.destination_time_map = defaultdict(deque)
        self.check_key = set()


    def addPacket(self, source: int, destination: int, timestampL: int) -> bool:
        packet = Packet(source, destination, timestampL)

        if f'{source}-{destination}-{timestampL}' in self.check_key:
            return False

        if len(self.storage) >= self.memoryLimit:
            oldest_packet = self.storage.popleft()
            self.destination_time_map[oldest_packet.destination].popleft()
            self.check_key.remove(f'{oldest_packet.source}-{oldest_packet.destination}-{oldest_packet.timestampL}')

        self.destination_time_map[destination].append(packet)
        self.storage.append(packet)
        self.check_key.add(f'{source}-{destination}-{timestampL}')
        return True

    def forwardPacket(self) -> list[int]:
        if self.storage:
            packet_forwarded = self.storage.popleft()
            self.destination_time_map[packet_forwarded.destination].popleft()
            self.check_key.remove(f'{packet_forwarded.source}-{packet_forwarded.destination}-{packet_forwarded.timestampL}')
            return packet_forwarded.tolist()
        return []




    def getCount(self, destination:int , startTime: int, endTime: int) -> int:
        arr = self.destination_time_map[destination]
        if not arr:
            return 0
        start = Packet(0,0 ,startTime)
        end = Packet(0,0 ,endTime)
        start_index = bisect.bisect_left(arr, start)
        end_index = bisect.bisect_right(arr, end)
        return end_index - start_index


a = Router(3)
print(a.addPacket(1, 4, 90)) # True
print(a.addPacket(2, 5, 90)) # True
print(a.addPacket(1, 4, 90)) # False
print(a.addPacket(3, 5, 95)) # True
print(a.addPacket(4, 5, 105)) # True
print(a.forwardPacket()) # [2, 5, 90]
print(a.addPacket(5, 2, 110)) # True
print(a.getCount(5, 100, 110)) # 1

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