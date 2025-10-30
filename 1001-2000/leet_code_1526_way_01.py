from ctypes import SetPointerType
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(target[i] - target[i-1], 0)
        return ans


print(Solution().minNumberOperations([1,2,3,2,1])) # 3
print(Solution().minNumberOperations([3,1,1,2])) # 4
print(Solution().minNumberOperations([3,1,5,4,2])) # 7