from collections import defaultdict, Counter
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if not sorted(words[i]) == sorted(words[i-1]):
                result.append(words[i])
        return result

print(Solution().removeAnagrams(words = ["abba","baba","bbaa","cd","cd"])) # ["abba","cd"]
print(Solution().removeAnagrams(words = ["a","b","c","d","e"])) # ["a","b","c","d","e"]