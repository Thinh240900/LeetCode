from collections import defaultdict


class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_vowels = {'a', 'e', 'i', 'u', 'o'}
        dict_vowels = defaultdict(int)
        dict_vowels['a'] = 0
        dict_consonant = defaultdict(int)
        dict_consonant['b'] = 0
        for char in s :
            if char in set_vowels:
                dict_vowels[char] += 1
            else:
                dict_consonant[char] += 1
        result = max(dict_vowels.values()) + max(dict_consonant.values())
        return result


print(Solution().maxFreqSum('successes')) # 6
print(Solution().maxFreqSum("aeiaeia")) # 3