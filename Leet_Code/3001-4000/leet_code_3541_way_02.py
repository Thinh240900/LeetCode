from collections import defaultdict


class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_vowels = {'a', 'e', 'i', 'u', 'o'}
        s = sorted(s)
        max_vowel = 0
        max_consonant = 0
        previous_char = ''
        current_count = 0
        for char in s:
            if char in set_vowels:
                if char == previous_char:
                    current_count += 1
                else:
                    current_count = 1
                    previous_char = char
                max_vowel = max(max_vowel, current_count)
            else:
                if char == previous_char:
                    current_count += 1
                else:
                    current_count = 1
                    previous_char = char
                max_consonant = max(max_consonant, current_count)

        return max_vowel + max_consonant


print(Solution().maxFreqSum('successes')) # 6
print(Solution().maxFreqSum("aeiaeia")) # 3