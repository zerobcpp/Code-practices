class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = defaultdict(int)
        for i in chars:
            c[i] += 1
        
        res = 0
        for w in words:
            need = True
            
            wc = defaultdict(int)
            for i in w:
                wc[i] += 1
            
            for i, v in wc.items():
                if c[i] < v:
                    need = False
                    break
            
            if need:
                res += len(w)
            
                    

        
        return res