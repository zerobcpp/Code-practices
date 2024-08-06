class Node:
    def __init__(self):
        self.node = {}
        self.cnt = 0
    
    def __repr__(self):
        return (f'{self.node}, {self.cnt}')
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, n):
        cur = self.root
        res = []
        for i in word:
            #print(cur)
            if i not in cur.node:
                cur.node[i] = Node()
                cur.node[i].cnt += 1
            else:
                cur.node[i].cnt += 1
                
            if cur.node[i].cnt == n:
                res.append(i)
            cur = cur.node[i]
        
        return res
        
    
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        trie = Trie()
        N = len(strs)
        for word in strs:
            res = max(res, trie.insert(word, N), key=len)
        
        return ''.join(res)
            
    
    def longestCommonPrefix(self, strs):
        res = strs[0]
        N = len(strs)
        print(res)
        for i in range(1, N):
            res = ''.join(res)
            while strs[i].startswith(res) == False:
                res = res[:-1]
                
        return ''.join(res)


           
        