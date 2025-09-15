class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        if locked[0] == '1' and s[0] == ')':
            return False
        if locked[-1] == '1' and s[-1] == '(':
            return False
        left = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                left += 1
            elif s[i] == ')':
                left -= 1
                if left < 0:
                    return False
        left = 0
        for i in range(len(s)-1 , 0, -1):
            if locked[i] == '0' or s[i] == ')':
                left += 1
            elif s[i] == '(':
                left -= 1
                if left < 0:
                    return False

        return True


# print(Solution().canBeValid("))()))", "010100")) # True
# print(Solution().canBeValid("))))))", "011100")) # False
print(Solution().canBeValid("))((()", "010110")) # False
# print(Solution().canBeValid("()()", "0000")) # True
# print(Solution().canBeValid(")", "0")) # False