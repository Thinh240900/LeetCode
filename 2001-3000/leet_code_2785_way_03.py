from collections import defaultdict, deque


class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        vowels_arr = []
        char_arr = []
        for char in s:
            if char in vowels:
                vowels_arr.append(char)
                char_arr.append(0)
            else:
                char_arr.append(char)
        vowels_arr.sort(reverse=True)
        for index in range(len(char_arr)):
            if char_arr[index]==0:
                char_arr[index] = vowels_arr.pop()
        return "".join(char_arr)


print(Solution().sortVowels("lEetcOde")) # LEOtcede
print(Solution().sortVowels("lYmpH")) # "lYmpH"