from collections import Counter


class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        odd = 0
        even = 100
        for key, value in count.items():
            if value % 2 == 1:
                if value > odd:
                    odd = value
            else:
                even = min(even, value)
        return odd  - even


print(Solution().maxDifference('aaaaabbc')) # 3
print(Solution().maxDifference("ddddddddddddddabcabcabccccc")) # 1