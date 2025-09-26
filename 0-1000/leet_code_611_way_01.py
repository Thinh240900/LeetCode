from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        count = 0
        for i in range(n-1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count

print(Solution().triangleNumber([2, 2, 3, 4]))  # Output: 3
print(Solution().triangleNumber([4,2,3,4]))  # Output: 4