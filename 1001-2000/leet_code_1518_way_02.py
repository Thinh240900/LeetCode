class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked = 0

        empty = 0
        full = numBottles

        while full :
            drinked += full
            empty += full

            full = empty // numExchange
            empty -= full * numExchange
        return drinked

print(Solution().numWaterBottles(9, 3)) # 13
print(Solution().numWaterBottles(15, 4)) # 19