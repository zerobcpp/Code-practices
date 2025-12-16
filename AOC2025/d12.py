from collections import defaultdict
import pulp
def convert_list(arr, toInt = False):
    N = len(arr)
    print(arr, N)
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
def LpgetMin(goal, conf):
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
    
            

with open('d12.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n\n')
#print(len(inputs))


grid = []
p1 = 0
import re
for i in inputs[:-1]:
    i = i.split(':')
    cnt = i[1].count('#')
    grid.append(int(cnt))


for i in inputs[-1].split('\n'):
    i = i.split(':')
    size = i[0].split('x')
    
    
    #print(arr)
    n, m = int(size[0]), int(size[1])
    area = n * m
    conf = [int(i) for i in i[1].split()]
    
    total = 0
    for j in range(len(conf)):
        total = conf[j] * grid[j]
        area -= total
        if area < 0:
            break
    
    if area >= 0:
        p1 += 1
    
    
#??? this was questioanble
print(p1)


