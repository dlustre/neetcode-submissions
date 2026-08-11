class Solution:
    def trap(self, height: List[int]) -> int:
        # for each index, store the nearest higher pillars from its left and from its right
        # iterate from left to right, at each index store prefix max. store current height as new max if bigger
        # same from right to left

        prefixes = [0] * len(height)
        suffixes = [0] * len(height)

        highestPrefix = 0 

        for i in range(len(height)):
            prefixes[i] = highestPrefix
            highestPrefix = max(highestPrefix, height[i])

        highestSuffix = 0
        for i in range(len(height), 0, -1):
            suffixes[i - 1] = highestSuffix
            highestSuffix = max(highestSuffix, height[i - 1])

        result = 0
        for i in range(len(height)):
            result += max(0, min(prefixes[i], suffixes[i]) - height[i])

        return result