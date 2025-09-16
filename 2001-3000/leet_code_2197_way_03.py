import math


class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
            Same way 01 but less append operation to reduce time complexity.
        """
        stack = []
        last = nums[0]
        for num in nums[1:]:

            if math.gcd(last, num) > 1:
                last = math.lcm(last, num)

                while stack and math.gcd(stack[-1], last) > 1:
                    last = math.lcm(stack.pop(), last)

            else:
                stack.append(last)
                last = num

        stack.append(last)
        return stack



print(Solution().replaceNonCoprimes([6,4,3,2,7,6,2])) # [12, 7, 6]
print(Solution().replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825])) # [2009,20677,825]
print(Solution().replaceNonCoprimes([2,2,1,1,3,3,3])) # [2, 1, 1, 3]