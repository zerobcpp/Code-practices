with open('d5.txt', 'r+') as f:
    inputs = f.read()

inputs = inputs.split('\n')

#print(inputs)

from collections import defaultdict
graph = defaultdict(set)
data = []
incorrect = []
#adj = defaultdict(int)


for i in inputs:
    if '|' in i:
        u, v = i.split('|')
        graph[u].add(v)
        graph['-1'].add(u)
        #adj[u] += 1
    elif i == '':
        continue
    else:
        data.append(i)
    
#print(graph)

def helper(data):
    page = 0
    idx = 0
    cur = -1
    take = True
    data = data.split(',')
    mid = len(data) // 2
    cur = '-1'
    
    for d in data:
        if d not in graph[cur]:
            
            take = False
            break
        if idx == mid:
            page = int(d)
        cur = d
        idx += 1
    
    #print(take, page)
    if not take:
        incorrect.append(data)
    return page if take else 0
    



p1 = 0
for d in data:
    p1 += helper(d)

def helper2(arr):
    
    N = len(arr)
    adj = defaultdict(int)
    
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] in graph[arr[j]]:
                adj[arr[i]] += 1
            if arr[j] in graph[arr[i]]:
                adj[arr[j]] += 1
    
    print(adj)
    start = []
    res = []
    for i in arr:
        if adj[i] == 0:
            start.append(i)
            res.append(i)
            

    while start:
        cur = start.pop()

        for neigh in graph[cur]:
            adj[neigh] -= 1
            if adj[neigh] == 0:
                res.append(int(neigh))
                start.append(neigh)
    
    return res[N//2]

print(graph)

p2 = 0
for inc in incorrect:
    p2 += helper2(inc)

print(p2)


#4818 too low