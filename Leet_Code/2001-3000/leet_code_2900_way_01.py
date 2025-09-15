class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        arr_0 = []
        flag_0 = 1
        arr_1 = []
        flag_1 = 0
        for i in range(len(words)):
            if groups[i] != flag_0:
                arr_0.append(words[i])
                flag_0 = groups[i]
            if groups[i] != flag_1:
                arr_1.append(words[i])
                flag_1 = groups[i]
        if len(arr_0) > len(arr_1):
            return arr_0
        else:
            return arr_1




print(Solution().getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1])) # ['e', 'b']
print(Solution().getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1])) # ['a', 'b', 'c']