class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        offset = 97

        counts = [0] * 26

        for char in s:
            counts[ord(char) - offset] += 1

        for char in t:
            counts[ord(char) - offset] -= 1

        for count in counts:
            if count != 0:
                return False
        
        return True