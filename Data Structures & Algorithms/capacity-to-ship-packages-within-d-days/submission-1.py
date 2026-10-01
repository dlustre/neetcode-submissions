class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(cap):
            currentWeight = 0
            daysSpent = 0

            for w in weights:
                newWeight = currentWeight + w

                if newWeight > cap:
                    daysSpent += 1
                    currentWeight = w
                else:
                    currentWeight = newWeight
            
            return daysSpent + 1 <= days


        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if condition(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low