import bisect
from collections import defaultdict, deque

## Fastest
## Fastest
## Fastest

class Router:
    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packets = {}  # key -> [source, destination, timestamp]
        self.counts = defaultdict(list)  # destination -> sorted list of timestamps
        self.queue = deque()  # FIFO order of packets

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)

        if key in self.packets:
            return False
        if len(self.packets) >= self.size:
            oldest_packet = self.queue.popleft()

            self.counts[self.packets.pop(oldest_packet)[1]].pop(0)

        self.queue.append(key)
        self.counts[destination].append(timestamp)
        self.packets[key] = [source, destination, timestamp]
        return True

    def forwardPacket(self) -> list:
        if not self.queue:
            return []
        key = self.queue.popleft()
        packet = self.packets.pop(key)
        self.counts[packet[1]].pop(0)
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.counts.get(destination, [])
        if not timestamps:
            return 0


        start_index = bisect.bisect_left(timestamps, startTime)


        end_index = bisect.bisect_right(timestamps, endTime)
        return end_index - start_index

    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        # Encode uniquely into 1 number
        return (source << 40) | (destination << 20) | timestamp

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