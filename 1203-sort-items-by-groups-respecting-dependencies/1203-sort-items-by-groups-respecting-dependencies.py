class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        def top_sort(nums, pre, suc):
            queue = deque([i for i in nums if not pre[i]])
            order = []
            
            while queue:
                cur = queue.popleft()
                order.append(cur)
                
                for child in suc[cur]:
                    pre[child].remove(cur)
                    
                    if not pre[child]:
                        queue.append(child)
                        
            return order if len(order) == len(nums) else []
        
        
        
        
        # group the items
        group_to_item = defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
                
            group_to_item[group[i]].add(i)
            
        
        
        item_pre, item_suc = defaultdict(set), defaultdict(set)   # same group items order
        group_pre, group_suc = defaultdict(set), defaultdict(set) # groups order
        
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    item_pre[i].add(j)
                    item_suc[j].add(i)
                    
                else:
                    group_pre[group[i]].add(group[j])
                    group_suc[group[j]].add(group[i])
                    
                    
        group_order = top_sort([i for i in group_to_item], group_pre, group_suc)
        
        ans = []
        for i in group_order:
            items = group_to_item[i]
            
            items_order = top_sort(items, item_pre, item_suc)
            
            if not items_order:
                return []
            ans += items_order
            
        return ans


        
        
                
                
        