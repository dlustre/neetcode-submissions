class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # maybe like sliding window
        # keep letter freqs
        # when starting a substring, keep track of letter(s) who have dupes ahead of it
        # only end the substring when there's no more letters in the group that have dupes ahead of it

        counts = Counter(s)
        result = []
        currentLength = 0
        charSet = set()

        for char in s:
            if not charSet:
                if currentLength > 0:
                    result.append(currentLength)

                currentLength = 0
            
            counts[char] -= 1
            currentLength += 1

            if counts[char] == 0:
                charSet.discard(char)
            else:
                charSet.add(char)
            
        result.append(currentLength)

        return result