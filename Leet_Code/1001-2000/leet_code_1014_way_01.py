class Solution(object):
    def __init__(self):
        self.result = -float('inf')
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                if values[i] + values[j] + i - j > self.result:
                    self.result = values[i] + values[j] + i - j
        return self.result

print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))  # Output: 11
print(Solution().maxScoreSightseeingPair([1, 2]))  # Output: 2