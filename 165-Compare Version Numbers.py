class Solution:
    def compareVersion(self, version1, version2):
        s1 = [int(i) for i in version1.split(".")]
        s2 = [int(i) for i in version2.split(".")]
        
        l1, l2 = len(s1), len(s2)
            
        print(s1, s2)
            
        return (s1 > s2) - (s1 < s2)