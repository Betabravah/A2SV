class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')
        for dir in dirs:
            if dir == '..':
                if stack:
                    stack.pop()
            elif dir != '.' and dir != '':
                stack.append(dir)

        return '/' + '/'.join(stack)
