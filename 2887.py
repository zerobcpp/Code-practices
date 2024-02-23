class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        strs = []
        for i in s:
            if i in vowels:
                strs.append(i)
        strs.sort(reverse = True)
        
        print(strs)
        res = []
        
        for i in s:
            if i in vowels:
                res.append(strs.pop())
            else:
                res.append(i)
        
        #print(res)
        
        return ''.join(res)
        
        
    def sortVowels(self, s):
        c = defaultdict(int)
        vowels = 'uoieaUOIEA'
        j = len(vowels) - 1
        for i in s:
            c[i] += 1
        
        res = []
        for i in s:
            if i not in vowels:
                res.append(i)
            else:
                
                while c[vowels[j]] <= 0 and j > 0:
                    j -= 1
                k = vowels[j]
                res.append(k)
                c[k] -= 1
        
        return ''.join(res)
            
                