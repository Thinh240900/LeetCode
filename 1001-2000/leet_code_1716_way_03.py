from calendar import day_abbr


class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7 :
            return (n * (n + 1)) // 2
        fullWeeks = n // 7
        ans = each = 28
        for i in range(1, fullWeeks):
            each += 7
            ans += each
        value_start_last_week = fullWeeks + 1
        remainder_days  = n - (fullWeeks * 7)
        for value in range(value_start_last_week, value_start_last_week+remainder_days):
            ans += value

        return ans


print(Solution().totalMoney(26)) # 135
print(Solution().totalMoney(10)) # 37
print(Solution().totalMoney(4)) # 10
print(Solution().totalMoney(20)) # 96
