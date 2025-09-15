from collections import defaultdict, deque


class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        vs = list(s)
        sorted_vowels = sorted([ch for ch in s if ch in vowels])
        idx = 0
        for i in range(len(vs)):
            if vs[i] in vowels:
                vs[i]= sorted_vowels[idx]
                idx += 1
        return ''.join(vs)

print(Solution().sortVowels("lEetcOde")) # LEOtcede
print(Solution().sortVowels("lYmpH")) # "lYmpH"