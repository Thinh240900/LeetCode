from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        curr = bank[0].count('1')
        beams = 0
        for row in bank[1:]:
            devices = row.count('1')
            if not devices:
                continue
            beams += curr * devices
            curr = devices
        return beams


print(Solution().numberOfBeams(bank = ["011001","000000","010100","001000"])) # 8
print(Solution().numberOfBeams(bank = ["000","111","000"])) # 0