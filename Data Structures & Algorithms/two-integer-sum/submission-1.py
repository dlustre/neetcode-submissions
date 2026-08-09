class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()

        for i, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], i]
            
            diffs[target - nums[i]] = i

        assert False, "Should not be here"