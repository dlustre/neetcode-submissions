class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,2,0]

        # maybe kinda like prefix sum
        # where prev indices can inform indices
        # ahead of it that it can be jumped to
        # so if it didnt have any predecessor
        # dont do anything with it

        isAccessible = [False] * len(nums)
        isAccessible[0] = True

        for i in range(len(nums)):
            if not isAccessible[i]:
                continue
            
            for jumpAhead in range(nums[i]):
                if i + jumpAhead + 1 > len(nums) - 1:
                    break
                isAccessible[i + jumpAhead + 1] = True

        return isAccessible[-1]