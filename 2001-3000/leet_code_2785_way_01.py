from collections import defaultdict, deque


class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = defaultdict(int)
        vowels_arr = deque(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        char_arr = []
        for char in s:
            if char in vowels_arr:
                dict[char] += 1
                char_arr.append(0)
            else:
                char_arr.append(char)
        result = ''
        for char in char_arr:
            if char!=0:
                result += char
            else:
                while not dict[vowels_arr[0]]:
                    vowels_arr.popleft()
                result += vowels_arr[0]
                dict[vowels_arr[0]] -= 1
        return result


print(Solution().sortVowels("lEetcOde")) # LEOtcede
print(Solution().sortVowels("lYmpH")) # "lYmpH"