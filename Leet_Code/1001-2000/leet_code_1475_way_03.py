class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        monoStack = []
        finalPrices = prices
        for i in range(len(prices) - 1, -1, -1):
            curr = prices[i]
            while len(monoStack) >= 1 and curr < monoStack[-1]:
                monoStack.pop(-1)

            if len(monoStack) >= 1:
                finalPrices[i] = curr - monoStack[-1]
            monoStack.append(curr)

        return finalPrices
print(Solution().finalPrices([8,4,6,5]))
