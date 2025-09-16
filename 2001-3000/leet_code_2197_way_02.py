import math


class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in nums:
            while stack:
                ucln = math.gcd(stack[-1], num)
                if ucln > 1:
                    num = stack[-1] * num // ucln
                    stack.pop()
                else:
                    break
            stack.append(num)

        return stack

print(Solution().replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825])) # [2009,20677,825]
print(Solution().replaceNonCoprimes([6,4,3,2,7,6,2])) # [12, 7, 6]
print(Solution().replaceNonCoprimes([2,2,1,1,3,3,3])) # [2, 1, 1, 3]