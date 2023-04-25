# 78 supplemental

# temp
s = "13142"
N = len(s)

def helper(idx, string = None):
    print(string, idx)
    if idx == N:
        return 1
    
    for i in range(idx, N):
        strs = s[idx:i+1]
        helper(i+1, strs)
    
    print('---')
    

helper(0)
        
        