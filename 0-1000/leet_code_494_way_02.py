class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        memo = [[0] * (2 * total + 1) for _ in range(len(nums))]

        def find_solution(index, sum, memo):
            if index == len(nums):
                if target == sum:
                    return 1
                else:
                    return 0
            else:
                if memo[index][sum + total]:
                    return memo[index][sum+total]
                a = find_solution(index + 1, sum + nums[index], memo)
                b = find_solution(index + 1, sum - nums[index], memo)
                memo[index][sum + total] = a + b
                return memo[index][sum+ total]

        return find_solution(0, 0, memo)

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 5))  # Output: 3
print(Solution().findTargetSumWays([5, 1, 5, 3, 1], 11))  # Output: 1
print(Solution().findTargetSumWays([1], 1))  # Output: 1
print(Solution().findTargetSumWays([4, 1, 5, 3, 1], 2)) # Output: 3
print(Solution().findTargetSumWays([2, 2, 3], -7))# Output: 1
