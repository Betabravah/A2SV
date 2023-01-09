class Solution:
    def multiply(self, num1:str, num2:str) -> str:
        product = 0
        for i, dig1 in enumerate(reversed(num1)):
            for j, dig2 in enumerate(reversed(num2)):
                n1 = int(dig1) * 10 ** i
                n2 = int(dig2) * 10 ** j
                product += n1 * n2

        return str(product)
