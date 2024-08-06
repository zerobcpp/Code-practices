class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        N = len(words)
        c = defaultdict(int)
        for i in words:
            for j in i:
                c[j] += 1
        print(c)
        for i, v in c.items():
            if v % N != 0:
                return False
        
        return True