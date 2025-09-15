class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        arr_0 = [words[0]]
        flag_0 = groups[0]
        for i in range(1, len(words)):
            if flag_0 != groups[i]:
                arr_0.append(words[i])
                flag_0 = groups[i]
        return arr_0





print(Solution().getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1])) # ['e', 'b']
print(Solution().getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1])) # ['a', 'b', 'c']