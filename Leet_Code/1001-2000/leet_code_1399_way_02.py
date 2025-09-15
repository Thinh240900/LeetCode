from collections import defaultdict


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashmap = [0] * 36
        gen = (i + j + k + h for i in range(10) for j in range(10) for k in range(10) for h in range(10))
        next(gen)
        for i in range(n):
            hashmap[next(gen)-1] += 1
        return hashmap.count(max(hashmap))


print(Solution().countLargestGroup(133)) # 4
print(Solution().countLargestGroup(13)) # 4
print(Solution().countLargestGroup(2)) # 2