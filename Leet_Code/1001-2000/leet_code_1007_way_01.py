from collections import defaultdict


class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        n = len(tops)
        dict_tops = defaultdict(int)
        dict_bottoms = defaultdict(int)
        dict_same = defaultdict(int)
        for i in range(n):
            if tops[i] != bottoms[i]:
                dict_tops[tops[i]] += 1
                dict_bottoms[bottoms[i]] += 1
            else :
                dict_same[tops[i]] += 1

        ans = n

        for i in range(1, 7):
            if dict_tops[i] + dict_bottoms[i] + dict_same[i] >= n:
                ans = min(ans, min(dict_tops[i], dict_bottoms[i]) )

        return ans if ans != n else -1



print(Solution().minDominoRotations([2,2,2,2,2,2], [5,2,6,2,3,2])) # 2
print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4])) # -1