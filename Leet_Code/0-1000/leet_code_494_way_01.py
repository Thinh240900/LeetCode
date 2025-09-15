class Solution(object):
    def __init__(self):
        self.result = 0
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_solution(index, sum):
            if index == len(nums):
                if target == sum:
                    self.result += 1
            else:
                find_solution(index + 1, sum + nums[index])
                find_solution(index + 1, sum - nums[index])

        find_solution(0, 0)

        return self.result

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
# print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 5))  # Output: 3
# print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 11))  # Output: 1
# print(Solution().findTargetSumWays([1], 1))  # Output: 1
# print(Solution().findTargetSumWays([4, 1, 5, 3, 1], 2))
# print(Solution().findTargetSumWays([2, 2, 3], -7))
