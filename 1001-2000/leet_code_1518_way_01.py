class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        result = 0
        while numBottles:
            result += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles // numExchange
            emptyBottles %= numExchange

        return result

print(Solution().numWaterBottles(9, 3)) # 13
print(Solution().numWaterBottles(15, 4)) # 19