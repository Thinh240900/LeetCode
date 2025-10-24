from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i



print(Solution().nextBeautifulNumber(1)) # 22
print(Solution().nextBeautifulNumber(1000)) # 1333
print(Solution().nextBeautifulNumber(3000)) # 3133