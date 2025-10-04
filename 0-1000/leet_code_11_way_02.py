from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_container = 0
        while left < right:
            if height[left] < height[right]:
                max_container = max(max_container, (right - left) * height[left])
                left += 1
            else:
                max_container = max(max_container, (right - left) * height[right])
                right -= 1
        return max_container



