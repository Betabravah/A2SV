class Solution:
    def findKthBit(self, n: int, k: int) -> str:
      
        def invert_string(string):
            inverted = ''
            for i in string:
                if i == '0':
                    inverted += '1'
                else:
                    inverted += '0'
            return inverted

          
        def get_string(index):
            if index == 1:
                return '0'
            else:
                return get_string(index - 1) + '1' + invert_string(get_string(index-1))[::-1]

        new_string = get_string(n)
        return new_string[k-1]
