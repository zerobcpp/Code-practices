class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        c = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }
        N = len(digits)
        res = []
        arr = []
        def helper(idx):
            #print(arr)
            if idx == N:
                res.append(''.join(arr[:]))
                return
            
            i = digits[idx]
            for char in c[i]:
                arr.append(char)
                helper(idx+1)
                arr.pop()
            
                
        
        helper(0)
        return res