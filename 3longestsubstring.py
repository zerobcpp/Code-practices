class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = [0] * 27
        left = right = 0
        count = 0
        for i in range(len(s)):
            rcptr = ord(s[right]) - ord('a')
            char[rcptr] += 1
            while char[rcptr] > 1:
                lcptr = ord(s[left]) - ord('a')
                char[lcptr] -= 1
                left += 1
            count = max(count, (right-left)+1)
            right += 1
        return count


    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        c = set()
        
        n = len(s)
        l = 0 
        for r in range(n):
            while s[r] in c:
                c.remove(s[l])
                l += 1
            
            c.add(s[r])
            res = max(res, len(c))
    
        return res

if __name__ == '__main__':
    print(Solution.lengthOfLongestSubstring(self = None, s = "abcabcbb"))
    print(Solution.lengthOfLongestSubver2(self=None, s="abcabcbb"))

