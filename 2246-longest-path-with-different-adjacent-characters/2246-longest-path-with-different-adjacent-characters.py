class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for idx, par in enumerate(parent):
            graph[par].append(idx)
        

        
        max_length = 1
        
        def dfs(idx):
            nonlocal max_length     
            
            best_subtree = 0
            second_best_subtree = 0
            

            for child in graph[idx]:
                subtree = dfs(child)
                                
                if s[child] != s[idx]:
                    
                    if subtree > best_subtree:
                        second_best_subtree = best_subtree
                        best_subtree = subtree
                        
                    elif subtree > second_best_subtree:
                        second_best_subtree = subtree
            
            # if path = left subtree -> current_node -> right subtree
            max_length = max(max_length, 1 + best_subtree + second_best_subtree)
            
            # if path = (left subtree or right subtree) -> current_node
            return best_subtree + 1
                
        dfs(0)
        
        return max_length
                
                
                
                
            
            
                