class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        number_after_add = {str(n):str((n+a)%10) for n in range(10)}

        def addOperation(s):
            res = ''
            for i in range(n):
                res += s[i] if i % 2 == 0 else number_after_add[s[i]]
            return res

        def rotateOperation(s):
            return s[n-b:] + s[:n-b]

        seen = set()
        def dfs(s):
            if s in seen :
                return

            seen.add(s)
            dfs(addOperation(s))
            dfs(rotateOperation(s))
            return

        dfs(s)
        return min(seen)

print(Solution().findLexSmallestString( s = "5525", a = 9, b = 2)) # 2050
print(Solution().findLexSmallestString(s = "74", a = 5, b = 1)) # 24
print(Solution().findLexSmallestString(s = "0011", a = 4, b = 2)) # 0011