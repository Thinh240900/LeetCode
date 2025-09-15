from math import comb


class Solution(object):
    def countBalancedPermutations(self, num):
        """
        :type num: str
        :rtype: int
        """
        MOD = 10**9 + 7
        nums = []
        total = 0
        for char in num:
            current_char = int(char)
            nums.append(current_char)
            total += current_char
        if total % 2 !=0:
            return 0

        target_sum = sum(nums) // 2
        freq = [0] * 10
        n = len(nums)
        max_odd_slot = (n+1) //2
        for i in nums :
            freq[i] += 1
        dpp = [[0] * (max_odd_slot + 1) for _ in range(target_sum+1 )]
        dpp[0][0] = 1
        slot_sum = total_sum = 0
        for i in range(10):
            slot_sum += freq[i]
            total_sum += freq[i] * i
            for odd_used_slot in range(
                    min(slot_sum, max_odd_slot),
                    max(0, slot_sum - (n - max_odd_slot)) -1,
                    -1
            ):
                even_remain_slot = slot_sum - odd_used_slot
                for curr in range(
                    min(total_sum, target_sum),
                    max(0, total_sum - target_sum) -1 ,
                    -1
                ):
                    res = 0
                    for j in range(
                        max(0, freq[i] - even_remain_slot),
                        min(freq[i], odd_used_slot) +1
                    ):
                        if i * j > curr:
                            break
                        ways = (
                            comb(odd_used_slot, j) * comb(even_remain_slot, freq[i] - j) % MOD
                        )
                        res = (
                                res + ways * dpp[curr - i * j][odd_used_slot - j] % MOD
                        ) % MOD
                        dpp[curr][odd_used_slot] = res % MOD

        return dpp[target_sum][max_odd_slot]

print(Solution().countBalancedPermutations("123")) # 2
print(Solution().countBalancedPermutations("112")) # 1
print(Solution().countBalancedPermutations("12345")) # 0