class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        result = 0
        even_num_n = n // 2
        odd_num_n = n - even_num_n
        even_num_m = m // 2
        odd_num_m = m - even_num_m
        result += (even_num_n * odd_num_m) + (odd_num_n * even_num_m)
        return result

print(Solution().flowerGame(3,2 )) # 3
print(Solution().flowerGame(1,1)) # 0