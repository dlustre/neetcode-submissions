class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(x):
            return sum(math.ceil(pile / x) for pile in piles) <= h
        
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            if condition(mid):
                high = mid
            else:
                low = mid + 1

        return low
