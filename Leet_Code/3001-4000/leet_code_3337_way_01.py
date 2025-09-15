from collections import deque

MOD = 10**9 + 7

class Mat:
    def __init__(self, copy_from: "Mat" = None):
        self.a = [[0] * 26 for _ in range(26)]
        if copy_from:
            for i in range(26):
                for j in range(26):
                    self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: "Mat"):
        result = Mat()
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    result.a[i][j] = (
                        result.a[i][j] +
                        self.a[i][k] * other.a[k][j]
                    ) % MOD
        return result

def I():
    m = Mat()
    for i in range(26):
        m.a[i][i] = 1
    return m

def quickmul(x: Mat, y: int):
    ans = I()
    cur = x
    while y:
        if y & 1:
            ans = ans * cur
        cur = cur * cur
        y >>= 1
    return ans

class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        T = Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1
                # T.a[i][(i + j) % 26] = 1

        res = quickmul(T, t)

        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord("a")] += 1

        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + res.a[i][j] * f[j]) % MOD

        return ans


print(Solution().lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])) # 7
print(Solution().lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])) # 8