class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        count_week = 0
        for i in range(1, n + 1):
            if (i-1) % 7 == 0:
                count_week += 1
            ans += (i-1) % 7 + count_week

        return ans


print(Solution().totalMoney(10)) # 37
print(Solution().totalMoney(4)) # 10
print(Solution().totalMoney(20)) # 96
print(Solution().totalMoney(26)) # 135