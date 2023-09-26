class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                
            cur = cur.children[i]
            
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        
        def traverse(node, index):
            if index == len(word):
                return node.is_end
            
            if word[index] == '.':
                for child in node.children:
                    if traverse(node.children[child], index + 1):
                        return True
                    
            if word[index] in node.children:
                return traverse(node.children[word[index]], index + 1)
                
                
        return traverse(self.root, 0)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)