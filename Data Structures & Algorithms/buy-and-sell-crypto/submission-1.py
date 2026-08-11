class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestPrefix = prices[0]
        result = 0

        for price in prices[1:]:
            result = max(result, price - cheapestPrefix)
            cheapestPrefix = min(cheapestPrefix, price)

        return result