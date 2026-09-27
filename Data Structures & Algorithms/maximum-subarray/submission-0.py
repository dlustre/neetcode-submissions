class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        result = currentSum

        for num in nums[1:]:
            take = currentSum + num
            reset = num

            currentSum = max(take, reset)
            result = max(result, currentSum)
        
        return result