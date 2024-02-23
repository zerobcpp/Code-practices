class TreeNode:
    def __init__(self):
        self.node = [None] * 27
        self.end = False
class Trie:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        x = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if not x.node[idx]:
                x.node[idx] = TreeNode()
            x = x.node[idx]
        x.end = True

    def search(self, word: str) -> bool:
        x = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if not x.node[idx]:
                return False
            x = x.node[idx]
        return x.end

    def startsWith(self, prefix: str) -> bool:
        x = self.root
        for i in prefix:
            idx = ord(i) - ord('a')
            if not x.node[idx]:
                return False
            x = x.node[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)