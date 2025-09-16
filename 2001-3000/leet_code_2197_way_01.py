import math


class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = [nums[0]]
        n = len(nums)


        for index in range(1, n):

            if math.gcd(stack[-1], nums[index]) > 1:
                examine = math.lcm(stack.pop(), nums[index])

                while stack and math.gcd(stack[-1], examine) > 1:
                    examine = math.lcm(stack.pop(), examine)

                stack.append(examine)
            else:
                stack.append(nums[index])

        return stack



print(Solution().replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825])) # [2009,20677,825]
print(Solution().replaceNonCoprimes([6,4,3,2,7,6,2])) # [12, 7, 6]
print(Solution().replaceNonCoprimes([2,2,1,1,3,3,3])) # [2, 1, 1, 3]