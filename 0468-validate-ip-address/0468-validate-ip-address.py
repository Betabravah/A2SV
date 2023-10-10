class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if '.' in queryIP:
            if ':' in queryIP:
                return "Neither"
            
            ipv4 = queryIP.split('.')
            
            if len(ipv4) != 4:
                return "Neither"
            
            for i in ipv4:
                if i.isdigit():
                    if len(i) != len(str(int(i))):
                        break
                    if not 0 <= int(i) <= 255:
                        break
                        
                else:
                    break
            else:
                return 'IPv4'
            
        
        if ':' in queryIP:
            if '.' in queryIP:
                return 'Neither'
            
            
            ipv6 = queryIP.split(':')
            
            if len(ipv6) != 8:
                return "Neither"
            
            for i in ipv6:
                if len(i) > 4:
                    break
                    
                try :
                    int(i, 16)
                except:
                    break
            else:
                return 'IPv6'
            
        return 'Neither'
                
            
            
        
            
            