class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text = text.split(' ')
        count = 0
        for word in text:
            if not any(c in brokenLetters for c in word):
                count += 1
        return count



print(Solution().canBeTypedWords(text = "hello world", brokenLetters = "ad")) # 1
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "lt")) # 1
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "e")) # 0