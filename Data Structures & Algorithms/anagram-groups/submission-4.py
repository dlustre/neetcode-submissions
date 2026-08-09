class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each str, create a character-count-key tuple to use as the key for a dict
        
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            
            for char in s:
                counts[ord(char) - ord("a")] += 1

            groups[tuple(counts)].append(s)

        return list(groups.values())