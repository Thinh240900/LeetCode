class Solution(object):
    count = 0
    ans=1
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """


        def dfs(num):
            if num > n:
                return
            self.count += 1
            if self.count == k:
                self.ans = num
            for i in range(10):
                dfs(num * 10 + i)

        for i in range(1, n + 1):
            if self.count >= k:
                return self.ans
            dfs(i)
        return self.ans

print(Solution().findKthNumber(100, 10))  # Output: 17
print(Solution().findKthNumber(1, 1))  # Output: 1
print(Solution().findKthNumber(2, 2))  # Output: 2
print(Solution().findKthNumber(13, 2))  # Output: 10
