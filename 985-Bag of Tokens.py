class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = 0
        tokens.sort()
        N = len(tokens)
        r = N - 1
        l = 0
        res = 0
        cnt = 0
        #print(tokens)
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                cnt += 1
            
            elif cnt > 0 and power < tokens[l]:
                power += tokens[r]
                cnt -= 1
                r -= 1
            else:
                break # can't do anythign with the current result
            #print(power, cnt, l, r)
            res = max(res, cnt)
        
        return res
            
            