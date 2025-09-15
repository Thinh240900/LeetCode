class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        heights = [0] * len(mat[0])
        result = 0
        for row in mat:
            for index, value in enumerate(row):
                heights[index] = 0 if value == 0 else heights[index] + 1
            stack = [[-1,0,-1]]
            for i, h in enumerate(heights):
                while stack[-1][2] >= h:
                    stack.pop()
                j, prev, _ = stack[-1]
                cur = prev + (i -j) * h
                stack.append([i, cur, h])
                result += cur
        return result


print(Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]])) # 13
print(Solution().numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])) # 24