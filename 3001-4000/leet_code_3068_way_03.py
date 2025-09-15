from jedi.inference.recursion import total_function_execution_limit


class Solution:
    def maximumValueSum(self, nums, k, edges) :
        max_negative = float('-inf')
        min_positive = float('inf')
        count_xor = 0
        total_sum = 0
        for num in nums:
            total_sum += num
            net_change = (num ^ k) - num
            # define if after xor is bigger than num
            if net_change > 0 :
                count_xor += 1
                min_positive = min(min_positive, net_change)
                total_sum += net_change
            else:
                max_negative = max(max_negative, net_change)
        if count_xor % 2 == 1:
            # - min_positive is remove 1 xor
            # + max_negative is add 1 xor
            return max(total_sum - min_positive, total_sum + max_negative)
        return total_sum



print(Solution().maximumValueSum(nums = [24,78,1,97,44], k = 6, edges = [[0,2],[1,2],[4,2],[3,4]])) # 260
print(Solution().maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]])) # 6
print(Solution().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]])) # 9
print(Solution().maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]])) # 42