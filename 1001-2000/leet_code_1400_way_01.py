class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq = [0]*26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        count_odd = 0
        for num in freq:
            if num % 2!= 0:
                count_odd += 1
        if count_odd > k:
            return False
        else:
            return True

print(Solution().canConstruct("annabelle", 2))
print(Solution().canConstruct("leetcode", 3))
print(Solution().canConstruct("true", 4))