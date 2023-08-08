#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        def get_chars(str1, str2):
            i = 0
            while i < min(len(str1), len(str2)):
                if str1[i] != str2[i]:
                    return (str1[i], str2[i])
                    
                i += 1
            return None
                
                
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for i in range(1, N):
            chars = get_chars(alien_dict[i-1], alien_dict[i])
            
            if chars:
                before, after = chars
                graph[before].append(after)
        
        
        queue = deque()
        for letters in graph.values():
            for char in letters:
                incoming[char] += 1
                
        for i in range(k):
            cur = chr(i + 97)
            if incoming[cur] == 0:
                queue.append(cur)
        
        ans = []        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for child in graph[cur]:
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    queue.append(child)
                    
        return ''.join(ans)
                
    # code here

    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends