class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1
        while ans < n:
            ans <<= 1
            ans = ans | 1
        return ans

print(Solution().smallestNumber(5)) # 7
print(Solution().smallestNumber(10)) # 15
print(Solution().smallestNumber(3)) # 3
