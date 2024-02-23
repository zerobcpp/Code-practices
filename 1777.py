class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        c = defaultdict(list)
        
        for i, v in c1.items():
            c[v].append(i)
            
        for i, v in c2.items():
            c[v].append(i)
        
        for i,v in c.items():
            if len(v) % 2 != 0:
                return False
        
        return True
