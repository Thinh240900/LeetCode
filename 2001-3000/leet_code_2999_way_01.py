from functools import reduce


class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        s_num = int(s)
        if s_num > finish:
            return 0
        str_start = str(start-1)
        str_finish = str(finish)


        def count(str_num):
            if len(str_num) < len(s):
                return 0
            if len(str_num) == len(s):
                return 1 if int(str_num) >= int(s) else 0
            pre_len = len(str_num) - len(s)
            suffix = str_num[pre_len:]
            count = 0

            for i in range(pre_len):
                if int(str_num[i]) > limit:
                    count += (limit+1) ** (pre_len -i)
                    return count
                count += int(str_num[i]) * (limit + 1) ** (pre_len - 1 - i)
            if int(suffix) >= int(s):
                count +=1

            return count

        return count(str_finish) - count(str_start)


# print(Solution().numberOfPowerfulInt(141, 148, 9, "9"))  # Output: 0
# print(Solution().numberOfPowerfulInt(14, 15, 9, "6"))  # Output: 0
# print(Solution().numberOfPowerfulInt(14, 99, 9, "13"))  # Output: 0
# print(Solution().numberOfPowerfulInt(86, 99, 9, "5"))  # Output: 1
# print(Solution().numberOfPowerfulInt(1, 16000, 4, "124"))  # Output: 10
# print(Solution().numberOfPowerfulInt(1, 6000, 4, "124"))  # Output: 5
# print(Solution().numberOfPowerfulInt(12,215,6,'10')) # 2
# print(Solution().numberOfPowerfulInt(12,215,6,'1')) # 2
# print(Solution().numberOfPowerfulInt(1000, 2000, 4, '3000')) # 0
# print(Solution().numberOfPowerfulInt(213, 544, 4, '2')) # 13
# print(Solution().numberOfPowerfulInt(213, 514, 4, '2')) # 13
# print(Solution().numberOfPowerfulInt(212, 544, 4, '2')) # 14
print(Solution().numberOfPowerfulInt(212, 344, 4, '2')) # 9
print(Solution().numberOfPowerfulInt(212, 341, 4, '2')) # 8


