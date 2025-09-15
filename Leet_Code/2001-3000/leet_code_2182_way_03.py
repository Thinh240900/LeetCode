import heapq as hq
import time

from collections import defaultdict
from xmlrpc.client import DateTime


class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        start = time.time()
        res = []

        freqs = defaultdict(int)

        for ele in s:
            freqs[ele] += 1

        heap = []
        hq.heapify(heap)

        for key, val in freqs.items():
            hq.heappush(heap, (-1 * ord(key), val))



        while heap:
            (ele, ct) = hq.heappop(heap)

            if not res or (res and chr(-1 * ele) != res[-1][-1]):
                res.append(chr(-1 * ele) * (min(repeatLimit, ct)))
                ct -= repeatLimit
                if ct > 0:
                    hq.heappush(heap, (ele, ct))
            elif not heap:
                break
            else:
                (ele2, ct2) = hq.heappop(heap)
                res.append(chr(-1 * ele2))
                ct2 -= 1
                if ct2 > 0:
                    hq.heappush(heap, (ele2, ct2))
                hq.heappush(heap, (ele, ct))

        return "".join(res)


print(Solution().repeatLimitedString("aababab", 2))
print(Solution().repeatLimitedString("cczazcc", 3))
print(Solution().repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy", 2))

