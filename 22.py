class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        arr = []
        def helper(op, cl):
            if op == cl and op == n:
                res.append(''.join(arr[:]))
            
            if op < n:
                arr.append('(')
                helper(op + 1, cl)
                arr.pop()
            if cl < op:
                arr.append(')')
                helper(op, cl + 1)
                arr.pop()
            
        
        helper(0, 0)
        return res