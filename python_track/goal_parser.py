class Solution:
    def interpret(self, command: str) -> str:
        parsed = ''
        i = 0
        while i < len(command):
            if command[i] == '(':
                if command[i+1] == ")":
                    parsed += 'o'
                    i += 2
                elif command[i+1] == 'a':
                    parsed += 'al'
                    i += 4
            else:
                parsed += command[i]
                i += 1

        return parsed
