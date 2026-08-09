class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(nums)

        # build a dict whose keys are (nums[i] - target) and values are i

        # if nums[i] can index into the dict, then return the current i with the indexed i.

        diffs = dict()

        for i, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], i]
            
            diffs[target - nums[i]] = i

        assert False, "Should not be here"