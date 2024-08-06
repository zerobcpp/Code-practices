class TreeNode:
    def __init__(self):
        self.node = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        x = self.root
        for i in word:
            if i not in x.node:
                x.node[i] = TreeNode()
            x = x.node[i]
        x.end = True

    def search(self, word: str) -> bool:
        x = self.root
        for i in word:
            if i not in x.node:
                return False
            x = x.node[i]
        return x.end

    def startsWith(self, prefix: str) -> bool:
        x = self.root
        for i in prefix:
            if i not in x.node:
                return False
            x = x.node[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)