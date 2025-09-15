class Solution(object):
    def __init__(self):
        self.result = -float('inf')
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        stack = values[-1] - len(values) +1
        for i in range(len(values)-2, -1, -1):
            if self.result < stack + values[i] + i:
                self.result = stack + values[i] + i
            if stack < values[i] - i:
                stack = values[i] - i

        return self.result

print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))  # Output: 11
print(Solution().maxScoreSightseeingPair([1, 2]))  # Output: 2
print(Solution().maxScoreSightseeingPair([5,3,2,6,2,6,37,4]))  # Output: 42
print(Solution().maxScoreSightseeingPair([1, 2, 3,66,1,8,6,9,4,6,4,7]))  # Output:72
print(Solution().maxScoreSightseeingPair([1,5,6,4,57,4,2, 2]))  # Output: 61
