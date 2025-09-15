from collections import defaultdict


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = defaultdict(int)
        for i in range(1, n+1):
            total = sum(int(digit) for digit in str(i))
            dict[total] += 1
        result = 0
        max_value = max(dict.values())
        for key, value in dict.items():
            if value == max_value:
                result +=1

        return result


print(Solution().countLargestGroup(13)) # 4
print(Solution().countLargestGroup(2)) # 2