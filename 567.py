class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)

        s1hash = [0] * 27
        s2hash = [0] * 27
        for i in s1:
            hashValue = ord(i) - ord('a')
            s1hash[hashValue] += 1

        for i in range(len(s2)-2):
            for j in range(size):
                hashValue = ord(s2[i+j]) - ord('a')
                s2hash[hashValue] += 1
            if s1hash == s2hash:
                return True
            # When it is not found, undone the change.
            for j in range(size):
                hashValue = ord(s2[i+j]) - ord('a')
                s2hash[hashValue] -= 1
        return False