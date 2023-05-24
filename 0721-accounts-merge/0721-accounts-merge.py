class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)
        group = {i:set(acc[1:]) for i, acc in enumerate(accounts)}
        user = {}
        
        
        
        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
                
            return root[node]
        
        
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            
            if rootx == rooty:
                return
            
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1
            
            
            if rank[rootx] > rank[rooty]:
                root[rooty] = rootx
                rank[rootx] += 1
                group[rootx].update(group[rooty])
                
            else:
                root[rootx] = rooty
                rank[rooty] += 1
                group[rooty].update(group[rootx])
                
                
                
                
        for idx, i in enumerate(accounts):
            
            emails = i[1:]
            for email in emails:
                usr = user.get(email, None)
                
                if usr != None:
                    union(usr, idx)
                    
                else:
                    user[email] = idx
        
        
        seen = set()
        ans = []
        for i in range(len(accounts)):
            parent = find(i)
            
            if parent not in seen:
                person = accounts[parent][0]
                emails = sorted(list(group[parent]))
                ans.append([person] + emails)
                seen.add(parent)
                
                
        return ans
        
            
             
                                
        