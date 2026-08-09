class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(formatted) - 1

        while left < right:
            if formatted[left] != formatted[right]:
                return False

            left += 1
            right -= 1

        return True