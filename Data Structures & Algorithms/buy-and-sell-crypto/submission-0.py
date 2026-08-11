class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # compute cheapest prefix day?
        # and track the highest profit based on sellPrice - cheapestPrefix

        cheapestPrefix = prices[0]
        result = 0

        for price in prices[1:]:
            result = max(result, price - cheapestPrefix)
            cheapestPrefix = min(cheapestPrefix, price)

        return result