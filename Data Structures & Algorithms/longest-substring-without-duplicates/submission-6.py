class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a sliding window that keeps growing via right pointer
        # if we find a duplicate, shift the left pointer until we dedupe that character
        # meanwhile we track the highest window width

        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.discard(s[left])
                left += 1
            
            charSet.add(s[right])
            result = max(result, right - left + 1)

        return result