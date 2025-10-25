class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        ans = 0
        for i in range(full_weeks):
            ans += 28 + 7 * i
        out_full_weeks = n % 7
        for i in range(out_full_weeks):
            ans += i + 1 + full_weeks
        return ans


print(Solution().totalMoney(26)) # 135
print(Solution().totalMoney(10)) # 37
print(Solution().totalMoney(4)) # 10
print(Solution().totalMoney(20)) # 96
