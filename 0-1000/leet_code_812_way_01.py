


class Solution(object):
    def largestTriangleArea(self, nums: list[list[int]]) -> float:
        n = len(nums)
        result = 0.0
        for i in range(n-2):
            x1,y1 = nums[i]
            for j in range(i+1, n-1):
                x2,y2 = nums[j]
                for k in range(j+1, n):
                    x3,y3 = nums[k]
                    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    if result < area:
                        result =area
        return result


print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
print(Solution().largestTriangleArea([[1,0],[0,0],[0,1]]))