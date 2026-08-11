class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed sliding window, where length is length of s1

        # keep a hash table of character counts one for each string, if they match, return true

        s1Counts = dict()
        s2Counts = dict()

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1Counts[s1[i]] = 1 + s1Counts.get(s1[i], 0)
            s2Counts[s2[i]] = 1 + s2Counts.get(s2[i], 0)

        left = 0
        offsetToEnd = len(s1) - 1


        def countsAreEqual(a, b):
            # print(a, b)
            if len(a) != len(b):
                return False
            
            for key in a:
                if a[key] != b.get(key, 0):
                    return False
            
            return True

        while left + offsetToEnd < len(s2):
            # print(s2[left:left+offsetToEnd + 1])
            if countsAreEqual(s1Counts, s2Counts):
                return True

            s2Counts[s2[left]] -= 1

            if s2Counts[s2[left]] == 0:
                del s2Counts[s2[left]]

            left += 1

            if left + offsetToEnd >= len(s2):
                break

            s2Counts[s2[left + offsetToEnd]] = 1 + s2Counts.get(s2[left + offsetToEnd], 0)

        return False

