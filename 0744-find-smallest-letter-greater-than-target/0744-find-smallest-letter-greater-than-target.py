class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = None
        
        for char in letters:
            if ord(char) > ord(target):
                if ans:
                    if ord(char) <= ord(ans):
                        ans = char
                else:
                    ans = char
                    
                
                
        return ans if ans else letters[0]