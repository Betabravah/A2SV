class Solution:
    def partition(self, s: str) -> List[List[str]]:            
        
        def backtrack(cur, idx):
            if idx == len(s):
                answer.append(cur.copy())
                return
            
            for i in range(idx, len(s)):
                temp = s[idx:i + 1]
                
                if temp == temp[::-1]:
                    cur.append(temp)
                    backtrack(cur, i + 1)
                    cur.pop()
                
                
                
                
        answer = []
        backtrack([], 0)
        return answer