class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        #res = []
        for i in strs:
            idx = str(sorted(i))
            c[idx].append(i)
        
#         for i, v in c.items():
#             res.append(v)
        
        return c.values()
    
    def groupAnagrams(self, strs):
        
        def convert(strs):
            arr = [0] * 27
            for i in strs:
                idx = ord(i) - ord('a')
                arr[idx] += 1
            return tuple(arr)
        
        c = defaultdict(list)
        for i in strs:
            c[convert(i)].append(i)
            
        
        return c.values()