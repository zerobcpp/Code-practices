class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
            
        ans = [] 
        def helper(pos,path):
            if len(path) == len(s):
                ans.append("".join(path))
                return 
             
            if s[pos].isalpha():
                helper(pos+1,path+[s[pos]])
                if 'a' <= s[pos] <= 'z':
                    helper(pos+1,path+[chr(ord(s[pos]) + ord('A')-ord('a'))])
                else:
                    helper(pos+1,path+[chr(ord(s[pos]) - ord('A')+ord('a'))])
            else:
                helper(pos+1,path+[s[pos]])
        
        helper(0,[])
        
        return ans 