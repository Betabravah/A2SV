class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        queue = deque(supplies)
        graph = defaultdict(list)
        count = defaultdict(int)
        
        for i in range(len(recipes)):
            for j in ingredients[i]:
                
                cur = recipes[i]
                graph[j].append(cur)
                count[cur] += 1
                
        
        output = []  
        while queue:
            cur = queue.popleft()
            
            for child in graph[cur]:
                count[child] -= 1
                
                if count[child] == 0:
                    queue.append(child) 
                    output.append(child)
                    
        return output
                    
            
            
            
            
            
            
            
            