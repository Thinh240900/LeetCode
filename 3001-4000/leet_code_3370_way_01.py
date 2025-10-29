
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x

print(Solution().smallestNumber(5)) # 7
print(Solution().smallestNumber(10)) # 15
print(Solution().smallestNumber(3)) # 3
