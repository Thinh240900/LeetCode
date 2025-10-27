from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        top = 0
        bot = 1
        n = len(bank)
        while bot < n:
            one_in_bot = bank[bot].count('1')
            if one_in_bot == 0:
                bot += 1
                continue

            ans += bank[top].count('1') * one_in_bot
            top = bot
            bot += 1
        return ans


print(Solution().numberOfBeams(bank = ["011001","000000","010100","001000"])) # 8
print(Solution().numberOfBeams(bank = ["000","111","000"])) # 0