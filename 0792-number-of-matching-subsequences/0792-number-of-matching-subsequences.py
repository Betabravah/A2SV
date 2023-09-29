class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        freq = defaultdict(list)
        
        for idx, i in enumerate(s):
            freq[i].append(idx)
            
        ans = 0
            
        for word in words:
            prev = -1
            
            for idx, i in enumerate(word):
                
                nearest = bisect_left(freq[i], prev)

                if nearest < len(freq[i]):
                    index = freq[i][nearest]
                    
                    if index >= prev:
                        prev = index + 1
                    else:
                        break
                    
                else:
                    break
                    
            else:
                ans += 1
                
        return ans
                