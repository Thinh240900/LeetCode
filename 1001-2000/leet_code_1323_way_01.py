class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        for char in num.__str__():
            if char == '6':
                return int(str(num).replace('6', '9', 1))
        return num
print(Solution().maximum69Number(9669))
print(Solution().maximum69Number(9996))
print(Solution().maximum69Number(9999))