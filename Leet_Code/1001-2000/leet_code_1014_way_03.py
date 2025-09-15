class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """

        left = 0
        right = 1
        ans = values[left] + values[right] - (right - left)

        while right < len(values) - 1:
            if values[right] >= values[left] - (right - left):
                left = right
                right += 1
            else:
                right += 1

            ans = max(ans, values[left] + values[right] - (right - left))

        return ans

# print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))  # Output: 11
# print(Solution().maxScoreSightseeingPair([1, 2]))  # Output: 2
print(Solution().maxScoreSightseeingPair([5,3,2,6,2,6,37,4]))  # Output: 42
print(Solution().maxScoreSightseeingPair([1, 2, 3,66,1,8,6,9,4,6,4,7]))  # Output:72
print(Solution().maxScoreSightseeingPair([1,5,6,4,57,4,2, 2]))  # Output: 61
