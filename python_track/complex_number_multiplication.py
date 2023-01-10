class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')

        x1, i1 = int(num1[0]), int(num1[1][:-1])
        x2, i2 = int(num2[0]), int(num2[1][:-1])

        x = x1 * x2
        i = (x1 * i2) + (x2 * i1)
        ii = (i1 * i2)

        real = x - ii
        im = i
        return str(real) + '+' + str(im) + 'i'
