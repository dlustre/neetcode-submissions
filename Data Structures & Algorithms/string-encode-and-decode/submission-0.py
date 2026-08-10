DELIMITER = "#"

class Solution:
    # protocol: words are encoded as a string of {length}#{word}, so we can expect every word to be prefixed with a number and a delimiter

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}{DELIMITER}{s}"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        pointer = 0

        while pointer < len(s):
            lengthStr = ""

            while s[pointer] != DELIMITER:
                lengthStr += s[pointer]
                pointer += 1
            
            wordLength = int(lengthStr)
            pointer += 1
            wordEnd = pointer + wordLength
            word = ""

            while pointer < wordEnd:
                word += s[pointer]
                pointer += 1
            
            decoded.append(word)

        return decoded