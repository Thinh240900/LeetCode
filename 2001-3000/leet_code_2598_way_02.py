from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        arr = [0] * value
        for num in nums:
            arr[num % value] += 1

        current_index = arr[0]
        remember_value = 0
        for i in range(1, len(arr)):
            if arr[i] < current_index:
                remember_value = i
                current_index = arr[i]

        return current_index*value + remember_value


print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 3))
print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5)) # 4
print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7)) # 2