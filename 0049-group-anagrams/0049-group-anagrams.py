class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for word in strs:
            freq = [0] * 26
            
            for i in word:
                freq[ord(i) - 97] += 1

            groups[tuple(freq)].append(word)
            
        return groups.values()