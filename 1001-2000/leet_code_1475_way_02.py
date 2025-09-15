class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                prices[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            stack.append(i)
        return prices

print(Solution().finalPrices([6,4,5]))