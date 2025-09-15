class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        set_broken_word = set([c for c in brokenLetters])
        text = text.split(' ')
        count = len(text)
        for word in text:
            if any(c in set_broken_word for c in word):
                count -= 1
        return count



print(Solution().canBeTypedWords(text = "hello world", brokenLetters = "ad")) # 1
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "lt")) # 1
print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "e")) # 0