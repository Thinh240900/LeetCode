from collections import defaultdict, deque


class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        sample = deque([0]) * 26
        MOD = 10**9 + 7
        for char in s:
            sample[ord(char) - 97] += 1
        for round in range(t):
            sample.appendleft(sample.pop())
            sample[1] += sample[0]
        return sum(sample) % MOD

print(Solution().lengthAfterTransformations(s = "abcyy", t = 2)) # 7
print(Solution().lengthAfterTransformations(s = "azbk", t = 1)) # 5