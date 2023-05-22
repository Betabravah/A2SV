class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = [i for i in range(26)]
        
        
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
                forbidden[rootx].update(forbidden[rooty])

            else:
                root[rootx] = rooty
                forbidden[rooty].update(forbidden[rootx])
                
                
        ans = True   
        forbidden = defaultdict(set)
        
        for i in equations:
            
            x, op, y = i[0], i[1], i[-1]
            x = ord(x) - ord('a')
            y = ord(y) - ord('a')
            rootx, rooty = find(x), find(y)
            
            
            if op == '=':
                if rootx not in forbidden[rooty]:
                    union(x, y)
                else:
                    return False
                
            else:
                
                if rootx == rooty:
                    return False
                
                forbidden[rootx].add(rooty)
                forbidden[rooty].add(rootx)
                
            
        return True
            
            
            
            
            
            
            
            
            
            