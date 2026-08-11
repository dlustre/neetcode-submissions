class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dynamic length sliding window
        # store character counts in hash table
        # every time we grow the window, check if we have high enough k to compensate for outlier characters
        # if we dont have high enough k, shift the left pointer until we satisfy requirements again

        left = 0
        result = 0
        counts = dict()

        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)

            while sum(sorted(counts.values(), reverse=True)[1:]) > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result