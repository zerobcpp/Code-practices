class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        size = len(s1)
        s1hash = [0] * 27
        s2hash = [0] * 27
        for i in range(size):
            s1hash[ord(s1[i]) - ord('a')] += 1
            s2hash[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2)-size):
            if s1hash == s2hash:
                return True
            s2hash[ord(s2[i+size]) - ord('a')] += 1
            s2hash[ord(s2[i]) - ord('a')] -= 1


        return s1hash == s2hash 