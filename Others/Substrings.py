from collections import defaultdict
def substring(s):
    N = len(s)
    c = defaultdict(int)
    for i in range(N):
        temp = []
        for j in range(i, N):
            temp.append(s[j])
            c[''.join(temp)] += 1
    
    print(c)
    return c

if __name__ == "__main__":
    c = substring("banana")
    
    v = sorted(c, key = lambda x:(c[x], len(x)), reverse=True)
    print(v)
    
            