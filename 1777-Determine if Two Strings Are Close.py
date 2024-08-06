class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        c = defaultdict(list)

        for i, v in c1.items():
            c[v].append((i, 1))
            
        for i, v in c2.items():
            c[v].append((i, 2))
        
        for i, v in c.items():
            if len(v) % 2 != 0:
                return False
            diff = 0
            for pair in v:
                if pair[1] == 1:
                    diff += 1
                else:
                    diff -= 1
            if diff != 0:
                return False
                
        
        for i, v in c1.items():
            if i not in c2:
                return False
        
        
        return True
    
    # O(N)
    # O(26) -> O(1)
    
    
