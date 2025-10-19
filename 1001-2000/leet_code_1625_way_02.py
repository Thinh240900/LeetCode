from math import gcd


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(map(int, s))
        n = len(s)
        step = gcd(b, n)
        g = gcd(a, 10)
        ans = [10]

        def modify(start: int ) -> None:
            ch = t[start]
            inc = ch % g - ch
            if inc:
                for j in range(start, n , 2 ):
                    t[j] = (t[j] + inc) % 10

        for i in range(0, n, step):
            t = s[i:] + s[:i]
            modify(1)
            if step % 2:
                modify(0)
            ans = min(ans, t)

        return ''.join(map(str, ans))

print(Solution().findLexSmallestString( s = "5525", a = 9, b = 2)) # 2050
print(Solution().findLexSmallestString(s = "74", a = 5, b = 1)) # 24
print(Solution().findLexSmallestString(s = "0011", a = 4, b = 2)) # 0011