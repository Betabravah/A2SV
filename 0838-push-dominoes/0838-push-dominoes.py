class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        lastPush = 0

        ans = []
        for curPush in range(1, len(dominoes)):
            if dominoes[curPush] == '.':
                continue
                
            if lastPush:
                ans.append(dominoes[lastPush])
                
            between = curPush - lastPush - 1
            
            if dominoes[lastPush] == dominoes[curPush]:
                ans.append(dominoes[lastPush] * between)
            elif dominoes[lastPush] == 'L' and dominoes[curPush] == 'R':
                ans.append('.' * between)
                
            else:
                ans.append('R' * (between // 2))
                ans.append('.' * (between % 2))
                ans.append('L' * (between // 2))
            
            lastPush = curPush
            
        return ''.join(ans)
                