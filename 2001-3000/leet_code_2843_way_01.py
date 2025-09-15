class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        result = 0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2 == 0:
                mid_point = len(s) // 2
                half_start = s[:mid_point]
                half_end = s[mid_point:]
                sum_half_start = sum(int(x) for x in half_start)
                sum_half_end = sum(int(x) for x in half_end)
                if sum_half_start == sum_half_end:
                    result += 1
        return result


print(Solution().countSymmetricIntegers(1, 100))
print(Solution().countSymmetricIntegers(1200, 1230))