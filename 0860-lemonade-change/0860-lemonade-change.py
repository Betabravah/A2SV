class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = ten = 0
        
        for i in bills:
            if i == 5:
                five += 1
                
            elif i == 10:
                ten += 1
                
                if five > 0:
                    five -= 1
                else:
                    return False
                    
            else:
                if ten:
                    ten -= 1
                    if five > 0:
                        five -= 1
                    else:
                        return False
                    
                else:
                    if five >= 3:
                        five -= 3
                    else:
                        return False
                    
        return True
                        
            
            