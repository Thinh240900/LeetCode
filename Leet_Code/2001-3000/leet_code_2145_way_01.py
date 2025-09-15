class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        arr = [lower]
        for diff in differences:
            arr.append(arr[-1] + diff)
        arr.sort()
        lowest = arr[0]
        highest = arr[-1]
        gap_low = abs(lower - lowest)
        gap_high = abs(upper - highest)
        if highest > upper:
            return 0
        return gap_high - gap_low + 1 if gap_high >= gap_low else 0
        # lowest_to_lower = lower - lowest
        # highest_to_upper = upper - highest
        # gap = upper - lower + 1
        #
        # if (lowest_to_lower and highest_to_upper) < 0:
        #     return 0
        # if lowest_to_lower > highest_to_upper:
        #     return gap // (lowest_to_lower - 1)


print(Solution().numberOfArrays([-11054,-29384,-79640], 21923, 53016)) # 2
print(Solution().numberOfArrays([1, -3, 4], 1, 6)) # 2
print(Solution().numberOfArrays([3,-4,5,1,-2], -4, 5)) # 4
print(Solution().numberOfArrays([4,-7,2], 3 ,6)) # 0