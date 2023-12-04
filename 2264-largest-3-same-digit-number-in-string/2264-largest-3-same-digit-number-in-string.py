class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left = 0
        count = defaultdict(int)
        
        for i in range(3):
            count[num[i]] += 1
            
            
        if len(count) == 1:
            prev_num = int(num[:3])
            ans = num[:3]
        else:
            ans = ''
            prev_num = 0
            
            
        for right in range(3, len(num)):
            
            if len(count) == 1:
                cur_num = int(num[left:right])
                
                if cur_num >= prev_num:
                    ans = num[left:right]
                    prev_num = cur_num
            
            
            count[num[left]] -= 1
            if count[num[left]] == 0:
                count.pop(num[left])
                
            left += 1
                
            count[num[right]] += 1
            
            
        if len(count) == 1:
            cur_num = int(num[left:])

            if cur_num >= prev_num:
                ans = num[left:]
                prev_num = cur_num
            
        return ans
            