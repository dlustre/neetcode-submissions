class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search: choose the middle element
        # if its bigger than the target, set the right pointer to the middle element - 1, vice versa

        left = 0
        right = len(nums) - 1

        while left <= right:
            print(nums[left:right + 1])
            mid = (left + right) // 2 # this feels wrong
            midNum = nums[mid]

            if midNum == target:
                return mid
            elif midNum < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1