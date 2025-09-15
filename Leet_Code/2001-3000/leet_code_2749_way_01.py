class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        if num2 > num1 :
            return -1

        def CountOne(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        for i in range(1, 61):
            temp = num1 - i *num2
            if temp  < i :
                return -1
            if i >= CountOne(temp):
                return i
        return -1

print(Solution().makeTheIntegerZero(110, 55)) # -1
print(Solution().makeTheIntegerZero(3, -2)) # 3
print(Solution().makeTheIntegerZero(5, 7)) # -1