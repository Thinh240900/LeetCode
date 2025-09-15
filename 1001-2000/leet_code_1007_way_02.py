from collections import defaultdict


class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """

        def count_rotations(target):

            top_rotation = bottom_rotation = 0

            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1

                if tops[i] != target:
                    top_rotation += 1

                if bottoms[i] != target:
                    bottom_rotation += 1

            return min(top_rotation, bottom_rotation)

        result = count_rotations(tops[0])

        if result != -1:
            return result

        return count_rotations(bottoms[0]) if tops[0] != bottoms[0] else -1



print(Solution().minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2])) # 2
print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4])) # -1