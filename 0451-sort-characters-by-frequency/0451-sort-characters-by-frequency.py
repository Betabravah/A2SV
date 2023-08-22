class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s).most_common()
        
        ans = []
        for char, ctr in freq:
            ans.append(char * ctr)
            
        return ''.join(ans)