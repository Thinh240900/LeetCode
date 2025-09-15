class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>0 and n%4==0:
            n=n//4
        return n==1

print(Solution().isPowerOfFour(16))
print(Solution().isPowerOfFour(5))
print(Solution().isPowerOfFour(1))