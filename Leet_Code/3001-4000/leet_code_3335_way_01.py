from collections import defaultdict


class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        sample = [0] * 26
        MOD = 10**9 + 7
        for char in s:
            sample[ord(char) - 97] += 1
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = sample[-1]
            nxt[1] = (sample[0] + sample[-1]) % MOD
            for i in range(2, 26):
                nxt[i] = sample[i-1]
            sample = nxt
        return sum(sample) % MOD

print(Solution().lengthAfterTransformations(s = "abcyy", t = 2)) # 7
print(Solution().lengthAfterTransformations(s = "azbk", t = 1)) # 5