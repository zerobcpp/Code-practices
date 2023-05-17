# 443. String Compression
 
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = 0
        r = 0
        while r < n:
            chars[l] = chars[r]
            count = 1
            while r + 1< n and chars[r] == chars[r+1]:
                count += 1
                r += 1
            
            if count > 1:
                for i in str(count):
                    chars[l+1] = i
                    l += 1
            
            l += 1
            r += 1
        
        return l