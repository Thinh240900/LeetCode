class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        ans = 0
        top_range = min(n, limit)
        for i in range(0, top_range+1):
            ans += max(0, min(limit, n-i) - max(0, n-i-limit)+1)
        return ans

print(Solution().distributeCandies(n = 5, limit = 2)) # 3
print(Solution().distributeCandies(n = 3, limit = 3)) # 10