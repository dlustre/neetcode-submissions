class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(formattedString) - 1

        while left <= right:
            if formattedString[left] != formattedString[right]:
                return False

            left += 1
            right -= 1

        return True