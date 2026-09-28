class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # look for a triplet are where one of its numbers
        # equals the target number, and the other two aren't larger than the target
        
        satisfied = [False, False, False]

        for t in triplets:
            for i in range(3):
                if t[i] == target[i] and t[(i + 1) % 3] <= target[(i + 1) % 3] and t[(i + 2) % 3] <= target[(i + 2) % 3]:
                    satisfied[i] = True

        return all(satisfied)