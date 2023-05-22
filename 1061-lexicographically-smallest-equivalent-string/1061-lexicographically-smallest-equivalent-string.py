class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = [i for i in range(26)]
        size = [1] * 26
        
        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
                
            return root[node]
        
        
        def union(x, y):
            
            rootx, rooty = find(x), find(y)
            
            if rootx == rooty:
                return
            
            if rootx < rooty:
                root[rooty] = rootx
                
            else:
                root[rootx] = rooty
                
        
        for i in range(len(s1)):
            char1, char2 = ord(s1[i]), ord(s2[i])
            union(char1 - ord('a'),  char2 - ord('a'))
        
        
        output = []
        for i in range(len(baseStr)):
            cur = find(ord(baseStr[i]) - ord('a'))
            output.append(chr(cur + ord('a')))
            
        return ''.join(output)
            
            
            
            
            
            
            
            
            