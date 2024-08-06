class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return None
        phash = [0] * 27
        shash = [0] * 27
        size = len(p)
        location = []
        for i in range(size):
            phash[ord(p[i]) - ord('a')] += 1 
            shash[ord(s[i]) - ord('a')] += 1
        i = -1
        
        for i in range(len(s) - size):
            if phash == shash:
                location.append(i)
            shash[ord(s[i+size]) - ord('a')] += 1 
            shash[ord(s[i]) - ord('a')] -= 1
        
        if phash == shash:
            location.append(i+1)
        
        return location
            

