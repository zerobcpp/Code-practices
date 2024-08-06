class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        res = []
        first = True
        for i in word:
            res.append(i)
            if i == ch and first:
                res = res[::-1]
                first = not first
            #print(res)
        
        return ''.join(res)
            