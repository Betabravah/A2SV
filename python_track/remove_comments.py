class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        whole = '\n'.join(source)+'\n'
        right = 0

        no_comments = ''
        while right < len(whole):
            if right+1 < len(whole) and whole[right:right+2] == "//":
                idx = whole.index('\n', right+2)
                right = idx
            elif right+1 <= len(whole) and whole[right:right+2] == '/*':
                idx = whole.index('*/', right+2)
                right = idx+2
            else:
                no_comments += whole[right]
                right += 1


        return [x for x in no_comments.split('\n') if x]
