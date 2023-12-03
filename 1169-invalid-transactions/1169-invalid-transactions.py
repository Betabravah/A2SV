class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = defaultdict(list)
        
        ans = set()
        
        for idx, i in enumerate(transactions):
            name, time, amount, city = i.split(',')
                
            trans[name].append((time, city, idx))
            
            if int(amount) > 1000:
                ans.add(idx)
            
        
        
        for name in trans:
            arr = trans[name]
            n = len(arr)
            
            for i in range(n):
                prev_time, prev_city, prev_idx = arr[i]
                
                for j in range(i+1, n):
                    cur_time, cur_city, cur_idx = arr[j]
                    
                    if abs(int(prev_time) - int(cur_time)) <= 60 and prev_city != cur_city:
                        ans.add(prev_idx)
                        ans.add(cur_idx)
                        
                        
        res = [transactions[i] for i in ans]
                
        return res
                
            