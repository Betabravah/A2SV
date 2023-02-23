class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_dic = {}
        s_dic={}
        for i in range(len(p)):
            p_dic[p[i]] = p_dic.get(p[i], 0) + 1
            s_dic[s[i]] = s_dic.get(s[i], 0) + 1

        _list = []
        window_end = len(p)
        window_start=0
        while(window_end<len(s)):
            if s_dic == p_dic:
                _list.append(window_start)
            s_dic[s[window_start]]-=1
            s_dic[s[window_end]]=s_dic.get(s[window_end], 0) + 1

            if(s_dic[s[window_start]]==0):
                s_dic.pop(s[window_start])
            window_start += 1
            window_end += 1
        if s_dic == p_dic:
            _list.append(window_start)
        
        return _list