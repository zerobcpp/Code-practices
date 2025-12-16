from collections import defaultdict
import pulp
def convert_list(arr, toInt = False):
    N = len(arr)
    for i in range(N):
        if toInt:
            arr[i] = [int(j) for j in inputs[i]]
        else:
            arr[i] = list(arr[i])
    return arr

def d8(x, y):
    cords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i or j:
                cords.append((x+i, y+j))
    return cords

d4 = [0, -1, 0, 1, 0]
dr = {
    0: [0, -1], #<
    1: [-1, 0], #^
    2: [0, 1],  #>
    3: [1, 0],  #v
}
# Linear algebra solver greed the minimal
def getMin(goal, conf):
    N = len(goal)
    V = len(conf)
    
    cur = pulp.LpProblem()
    A = [pulp.LpVariable(str(i), lowBound=0, cat="Integer") for i in range(V)]
    #rint(goal, conf)
    cur += pulp.lpSum(A)
    c = defaultdict(set)
    
    for i in range(len(conf)):    
        for j in conf[i]: 
            c[j].add(i)
    
    #print(c, A)
    for i, v in c.items():
        cur += pulp.lpSum([A[j] for j in v]) == goal[i]
    cur.solve()
    #print(cur)
    cnt = 0
    for i in A:
        cnt += i.value()
    return cnt
    
            

with open('d11.txt', 'r+') as f:
    inputs = f.read()
inputs = inputs.split('\n')

graph = defaultdict(list)

for i in inputs:
    i = i.split(':')
    u = i[0]
    child = i[1].split()
    
    for j in child: 
        graph[u].append(j)
        
def part1():

    #print(graph)
    
    def dfs(parent):
        st = [parent]
        
        
        cnt = 0
        while st:
            cur = st.pop()
            if cur == 'out':
                cnt += 1

            for neigh in graph[cur]:
                st.append(neigh)
        
        
        return cnt
    
    res = 0
    for i in graph['you']:
        res += dfs(i)
    
    print(res)
    return res

def part2():
    cache = {}
    
    def helper(c, cnt):
        
        #print(c, cnt)
        if c == 'out' and cnt == 2:
            return 1
        cnt += 1 if c in ['fft', 'dac'] else 0
        if (c, cnt) in cache:
            return cache[c, cnt]
        ways = 0
        for neigh in graph[c]:
            ways += helper(neigh, cnt)
        cache[c, cnt] = ways
        return ways
    
    res = 0
    for child in graph['svr']:
        res += helper(child, 0)
    print(res)
    return res
        
        
part1()
part2()


        



