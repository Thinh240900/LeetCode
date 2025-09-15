class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Base case: both strings are empty
        if not str1 and not str2:
            return ""

        # Base case: one string is empty, append the other string
        if not str1:
            return str2
        if not str2:
            return str1

        if str1[0] == str2[0]:
            return str1[0] + self.shortestCommonSupersequence(str1[1:], str2[1:])
        else:
            pick_str1 = str1[0] + self.shortestCommonSupersequence(str1[1:],str2)
            pick_str2 = str2[0] + self.shortestCommonSupersequence(str1, str2[1:])

        return pick_str1 if len(pick_str1) < len(pick_str2) else pick_str2

print(Solution().shortestCommonSupersequence('abac', 'cab'))
print(Solution().shortestCommonSupersequence('aaaaaaaa', 'aaaaaaaa'))
print(Solution().shortestCommonSupersequence('bbbaaaba', 'bbababbb'))