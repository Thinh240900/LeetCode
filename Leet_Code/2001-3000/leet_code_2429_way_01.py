class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count2 = num2.bit_count()
        count1 = num1.bit_count()
        if count2 == count1:
            return num1
        if count1 > count2:
            result = num1
            while count1 > count2:


print(Solution().minimizeXor(3, 5))  # Output: 3
print(Solution().minimizeXor(12, 1))  # Output: 3