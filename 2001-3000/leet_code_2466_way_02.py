class Solution(object):
    def __init__(self):
        self.result = 0
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        mod = 10**9 + 7
        arr = [0 for _ in range(high + 1)]
        arr[0] = 1
        # arr[zero] += 1
        # arr[one] += 1
        for i in range(1, high +1):
            if i - zero >= 0:
                arr[i] += arr[i - zero]
            if i - one >= 0:
                arr[i] += arr[i - one]
            arr[i] %= mod

        return sum(arr[low:high + 1]) % mod

print(Solution().countGoodStrings(3, 3, 1, 1))
print(Solution().countGoodStrings(2, 3, 1, 2))
print(Solution().countGoodStrings(10, 10, 2, 1))
