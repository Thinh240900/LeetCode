from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        output = 0
        while left < right:
            if height[left] < height[right]:
                if (right - left) * height[left] > output:
                    output = (right - left) * height[left]
                left += 1
            elif height[left] > height[right]:
                if (right - left) * height[right] > output:
                    output = (right - left) * height[right]
                right -= 1
            else:
                if (right - left) * height[left] > output:
                    output = (right - left) * height[left]
                left += 1
        return output



