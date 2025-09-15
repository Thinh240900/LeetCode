from collections import defaultdict


class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """

        n = len(words)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0

        def check(a, b):
            if len(a) != len(b):
                return False
            diff = 0
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            if diff == 1:
                return True
            return False

        for i in range(1, n):
            for j in range(i):
                if (check(words[j], words[i])
                and groups[j] != groups[i]
                and dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
                    prev_[i] = j
            if dp[i] > dp[max_index] :
                max_index = i

        ans = []
        while max_index >=0:
            ans.append(words[max_index])
            max_index = prev_[max_index]
        ans.reverse()
        return ans

print(Solution().getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2]))
print(Solution().getWordsInLongestSubsequence(words = ["a","b","c","d"], groups = [1,2,3,4]))