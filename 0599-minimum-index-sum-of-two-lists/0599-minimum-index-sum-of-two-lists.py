class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {}
        for idx, word in enumerate(list1):
            if word in index:
                index[word] = min(index[word], idx)
            else:
                index[word] = idx
                
        ans, ctr = [], float('inf')
        for idx, word in enumerate(list2):
            if word in index:
                cur_sum = index[word] + idx
                if cur_sum < ctr:
                    ans = [word]
                    ctr = cur_sum
                elif cur_sum == ctr:
                    ans.append(word)
                    
        return ans
                    
                    