from collections import defaultdict


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict_word = defaultdict(int)
        set_word = set()
        for word in words:
            if dict_word[word] == 0:
                set_word.add(word)
            dict_word[word] += 1
        ans = 0
        duplicate_word = set()
        for word in set_word:
            if word[0] != word[1]:
                min_value = min(dict_word[word], dict_word[word[::-1]])
                ans += min_value * 4
                dict_word[word] = 0
                dict_word[word[::-1]] = 0
            else:
                duplicate_word.add(word)
        for word in duplicate_word:
            if dict_word[word] >1:
                ans += (dict_word[word] // 2 ) * 4
                dict_word[word] = dict_word[word] % 2
        for key, value in dict_word.items():
            if key[0] == key[1] and value > 0 :
                ans += 2
                break
        return ans




print(Solution().longestPalindrome(words = ["bb","bb"])) # 4
print(Solution().longestPalindrome(words = ["lc","cl","gg"])) # 6
print(Solution().longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"])) # 8
print(Solution().longestPalindrome(words = ["cc","ll","xx"])) # 2