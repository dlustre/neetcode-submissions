class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a sliding window that keeps growing via right pointer
        # if we find a duplicate, shift the left pointer until we dedupe that character
        # meanwhile we track the highest window width

        if len(s) == 0:
            return 0

        charSet = set(s[0])
        left = 0
        right = 0
        result = 1

        while right < len(s):
            right += 1

            if right >= len(s):
                return result


            if s[right] in charSet:
                while s[left] != s[right]:
                    charSet.discard(s[left])
                    left += 1
                if left != right:
                    left += 1
            
            charSet.add(s[right])
            # print(f"{s[left:right + 1]} ({charSet})")

            result = max(result, len(charSet))

        return result