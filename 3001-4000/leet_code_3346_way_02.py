from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxVal = max(nums) + k + 2
        count = [0] * maxVal

        for v in nums:
            count[v] += 1

        for i in range(1, maxVal):
            count[i] += count[i - 1]

        res = 0
        for i in range(maxVal):
            left = max(0, i - k)
            right = min(maxVal - 1, i + k)
            total = count[right] - (count[left - 1] if left else 0)
            freq = count[i] - (count[i - 1] if i else 0)
            res = max(res, freq + min(numOperations, total - freq))

        return res


print(Solution().maxFrequency(nums = [1,4,5], k = 1, numOperations = 2)) # 2
print(Solution().maxFrequency(nums = [5,11,20,20], k = 5, numOperations = 1)) # 2