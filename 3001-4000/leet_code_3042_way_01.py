class Solution(object):
    def isPrefixAndSuffix(self, str1, str2):
        if str2.startswith(str1) and str2.endswith(str1):
            return 1
        return 0
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) <= len(words[j]):
                    count += self.isPrefixAndSuffix(words[i], words[j])
        return count


print(Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(Solution().countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(Solution().countPrefixSuffixPairs(["abab","ab"]))

