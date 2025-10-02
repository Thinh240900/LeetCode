class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drinked = numBottles
        empty = numBottles
        while empty >= numExchange:
            drinked += 1
            empty -= numExchange -1
            numExchange += 1
        return drinked


print(Solution().maxBottlesDrunk(13, 6))
print(Solution().maxBottlesDrunk(10, 3))