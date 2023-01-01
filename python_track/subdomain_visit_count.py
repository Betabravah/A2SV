class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        _dict = {}
        for i in range(len(cpdomains)):
            [count, domain] = cpdomains[i].split(' ')
            count = int(count)
            
            left, middle, right = 0, 0, len(domain) - 1
            while middle < right:
                if domain[middle] == '.':
                    dom = domain[left:right+1]
                    _dict[dom] = count + _dict.get(dom, 0)
                    left = middle + 1
                middle += 1

            dom = domain[left:right+1]
            _dict[dom] = count + _dict.get(dom, 0)


        output = []
        for key in _dict.keys():
            domain = str(_dict[key]) + ' ' + key
            output.append(domain)

        return output
