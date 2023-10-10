class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        freq1 = Counter(s1)
        freq2 = defaultdict(int)
        
        for i in range(len(s1)):
            freq2[s2[i]] += 1
        
        left, right = 0, len(s1)
        
        while right < len(s2):
            if freq1 == freq2:
                return True
                
            freq2[s2[right]] += 1
            freq2[s2[left]] -= 1
            
            if freq2[s2[left]] == 0:
                freq2.pop(s2[left])
                
            left += 1
            right += 1
               
                
        if freq1 == freq2:
            return True
        
        return False
            