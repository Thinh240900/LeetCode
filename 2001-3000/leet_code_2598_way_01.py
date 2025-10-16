from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        ans = 0
        arr = [0] * value
        for num in nums:
            arr[num % value] += 1
        while True:
            current = ans % value
            if arr[current]:
                arr[current] -= 1
                ans += 1
            else:
                return ans


print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5)) # 4
print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7)) # 2