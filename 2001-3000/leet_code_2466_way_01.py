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
        test = ''
        real_zero = zero * '0'
        real_one = one * '1'
        def find_solution(target, sum):
            if len(sum) == target:
                self.result += 1
            if len(sum) > target:
                return
            find_solution(target, sum + real_zero)
            find_solution(target, sum + real_one)

        for i in range(low, high + 1):
            find_solution(i, test)
        return self.result
print(Solution().countGoodStrings(3, 3, 1, 1))
print(Solution().countGoodStrings(2, 3, 1, 2))
