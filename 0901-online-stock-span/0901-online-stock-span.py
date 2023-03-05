class StockSpanner:

    def __init__(self):
        self.span = []
    def next(self, price: int) -> int:
        # print(self.span)
        ctr = 1
        while self.span and self.span[-1][0] <= price:
            ctr += self.span.pop()[1]

        self.span.append([price, ctr])
            
        return ctr


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)