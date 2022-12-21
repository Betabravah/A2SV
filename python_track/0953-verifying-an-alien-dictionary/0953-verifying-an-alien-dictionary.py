class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not self.check(words[i], words[j], order):
                    return False
        return True

    def check(self, word1, word2, order):
        i = 0
        length = min(len(word1), len(word2))
        while i < length:
            if order.index(word1[i]) < order.index(word2[i]):
                return True
            elif order.index(word1[i]) == order.index(word2[i]):
                i += 1
            else:
                return False
        if len(word1) <= len(word2):
            return True
        else:
            return False

