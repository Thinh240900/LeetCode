class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        MaxPowerOfThree = 1162261467
        return n>0 and MaxPowerOfThree % n == 0

print(Solution().isPowerOfThree(27)) # true
print(Solution().isPowerOfThree(0)) # false
print(Solution().isPowerOfThree(-1)) # false