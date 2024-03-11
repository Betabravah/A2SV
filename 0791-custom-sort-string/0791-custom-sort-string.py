class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        seen = set()
        
        ans = []
        for i in order:
            if i in freq:
                ans.append(i * freq[i])
                seen.add(i)
                
        
        for i in freq:
            if i not in seen:
                ans.append(i * freq[i])
                seen.add(i)
                
        return ''.join(ans)