class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # iterate through nums

        # for each element, 'backtrack' by creating a subset that doesn't have it and one that does

        # do the above with a recursive helper

        result = [[]]

        def backtrack(i, subset):
            if i >= len(nums):
                return

            backtrack(i + 1, subset)
            subsetWithNum = subset + [nums[i]]
            result.append(subsetWithNum)
            backtrack(i + 1, subsetWithNum)

        backtrack(0, [])

        return result