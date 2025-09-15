class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arr = ''
        i=0
        j=0
        while i < len(word1) and j < len(word2):
            arr += word1[i]
            arr += word2[j]
            i += 1
            j += 1
        if len(word1) < len(word2):
            arr += word2[i:]
        else:
            arr += word1[i:]
        return arr

print(Solution().mergeAlternately("abc", "def"))
print(Solution().mergeAlternately("ab", "pqrs"))