class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        res = 0
        N = len(word)
        for i in range(N):
            c = {'a': 0, 'e': 0, 'i': 0, 'o' : 0, 'u' : 0}
            for j in range(i, N):
                idx = word[j]
                if idx in c:
                    c[idx] += 1
                else:
                    break
                if all(c[i] >= 1 for i in c):
                    res += 1
                    #print(c)
            #print()
        return res

        
        