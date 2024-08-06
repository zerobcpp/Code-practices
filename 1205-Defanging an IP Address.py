class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for i in address:
            if i == '.':
                res.extend('[.]')
            else:
                res.append(i)
        
        return ''.join(res)