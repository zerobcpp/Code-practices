class Trie:

    def __init__(self):
        self.child = {}
        self.end = False


class Solution:
    def __init__(self):
        self.root = Trie()
        self.length = 0

    def insert(self, word):
        x = self.root
        for w in word:
            if w not in x.child:
                x.child[w] = Trie()
            x = x.child[w]
        x.end = True
        self.length = max(self.length, len(word))
        return None

    def search(self, word):
        n = len(word)

        def helper(idx, node):
            for i in range(idx, n):
                cidx = word[i]
                if cidx == '*':
                    for child in node.child.values():
                        if helper(idx + 1, child):
                            return True
                        return False
                else:
                    if cidx not in node.child:
                        return False
                    node = node.child[cidx]
            return node.end
