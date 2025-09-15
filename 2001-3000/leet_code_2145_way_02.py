class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        x = 0
        l, u = 0, 0
        for i in differences:
            x += i
            if x < l:
                l = x
            if x > u:
                u = x
        return max(0, upper - u - lower + l + 1)

print(Solution().numberOfArrays([3,-4,5,1,-2], -4, 5)) # 4
print(Solution().numberOfArrays([1, -3, 4], 1, 6)) # 2
print(Solution().numberOfArrays([4,-7,2], 3 ,6)) # 0
print(Solution().numberOfArrays([-11054,-29384,-79640], 21923, 53016)) # 2
