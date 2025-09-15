from collections import defaultdict


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        ans = 0
        dict = defaultdict(int)
        for domino in dominoes:
            key = tuple(sorted(domino))
            ans += dict[key]
            dict[key] += 1
        return ans

print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])) # 1
print(Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])) # 3