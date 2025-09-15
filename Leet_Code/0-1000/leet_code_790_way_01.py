from collections import defaultdict


class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = defaultdict(int)
        dict[1] =1
        dict[0] = 1
        for i in range(1, n):
            dict[i+1] = 2*dict[i] + dict[i-2]
        return dict[n]

print(Solution().numTilings(3))
print(Solution().numTilings(1))