class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, subset):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subsetWithNum = subset + [nums[i]]
            backtrack(i + 1, subsetWithNum)
            backtrack(i + 1, subset)

        backtrack(0, [])

        return result