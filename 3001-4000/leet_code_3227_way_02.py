class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        set_vowels = {'a', 'e', 'i', 'o', 'u'}
        for char in s:
            if char in set_vowels:
                return True
        return False


print(Solution().doesAliceWin("leetcoder")) # true
print(Solution().doesAliceWin("bbcd")) # false