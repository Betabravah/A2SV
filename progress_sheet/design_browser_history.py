class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.list = ListNode(homepage)
        self.cur = self.list

    def visit(self, url: str) -> None:
        newURL = ListNode(url)
        newURL.prev = self.cur
        self.cur.next = newURL
        self.cur = newURL

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
