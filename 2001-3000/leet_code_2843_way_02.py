class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for i in range(low, high+1):
            if i < 100 and i % 11 ==0:
                count += 1
            elif i > 1000:
                half_start = i // 1000 + i % 1000 // 100
                half_end = i % 100 // 10 + i % 10
                if half_start == half_end:
                    count += 1
        return count


print(Solution().countSymmetricIntegers(1, 100))
print(Solution().countSymmetricIntegers(1200, 1230))