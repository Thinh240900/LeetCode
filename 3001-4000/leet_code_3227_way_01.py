class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_vowels = 0
        set_vowels = {'a', 'e', 'i', 'o', 'u'}
        for char in s:
            if char in set_vowels:
                count_vowels += 1
        return count_vowels > 0


print(Solution().doesAliceWin("leetcoder")) # true
print(Solution().doesAliceWin("bbcd")) # false