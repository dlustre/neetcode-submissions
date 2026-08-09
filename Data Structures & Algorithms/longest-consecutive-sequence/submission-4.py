class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find parents (every num that doesn't have a num - 1)
        # for parent in parents
        # if parent + 1 in nums set

        numsSet = set(nums)
        starts = [num for num in nums if num - 1 not in numsSet]

        result = 0

        for start in starts:
            currentCount = 1
            target = start + 1
            while target in numsSet:
                currentCount += 1
                target += 1

            result = max(result, currentCount)
            
        return result