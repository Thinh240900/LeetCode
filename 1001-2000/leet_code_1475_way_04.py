class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        result = prices
        for i in range(len(prices)-1, -1, -1):
            cur = prices[i]
            while stack and prices[i] < stack[-1]:
                stack.pop()
            if stack and stack[-1] <= prices[i]:
                result[i] -= stack[-1]
            stack.append(cur)

        return result

print(Solution().finalPrices([8,7,4,6,5]))
