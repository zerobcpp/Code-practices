class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        strs = []
        for i in s:
            if i in vowels:
                strs.append(i)
        strs.sort(reverse = True)
        
        res = []
        
        for i in s:
            if i in vowels:
                res.append(strs.pop())
            else:
                res.append(i)
        
        #print(res)
        
        return ''.join(res)
        