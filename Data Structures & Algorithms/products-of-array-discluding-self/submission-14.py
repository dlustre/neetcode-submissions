class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # store products from left to mid, and products from right to mid
        fromLeft = []
        fromRight = []

        for i, num in enumerate(nums):
            if i == 0:
                fromLeft.append(num)
            else:
                fromLeft.append(num * fromLeft[-1])
        
        for i, num in enumerate(reversed(nums)):
            if i == 0:
                fromRight.append(num)
            else:
                fromRight.append(num * fromRight[-1])

        fromRight.reverse()

        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(fromRight[i + 1])
            elif i == len(nums) - 1:
                result.append(fromLeft[i - 1])
            else:
                result.append(fromLeft[i - 1] * fromRight[i + 1])

        return result