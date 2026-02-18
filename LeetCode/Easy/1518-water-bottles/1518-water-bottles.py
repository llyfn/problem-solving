class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            x = numBottles // numExchange
            ans += x * numExchange
            numBottles -= x * (numExchange - 1)
        ans += numBottles
        return ans
