class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        # sort list so we can replicate 2sum
        # because we can find two integers that equal -nums[i]

        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = num + nums[left] + nums[right]
                
                if threeSum == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return result