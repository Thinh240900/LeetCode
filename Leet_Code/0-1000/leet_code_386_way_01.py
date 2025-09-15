class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        def dfs(num):
            if num > n:
                return
            res.append(num)
            for i in range(10):
                dfs(num * 10 + i)

        for i in range(1, 10):
            dfs(i)
        return res

print(Solution().lexicalOrder(13)) # [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, ]
print(Solution().lexicalOrder(2)) # [1, 2]