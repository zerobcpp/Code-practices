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

from collections import defaultdict, deque
import numpy as np
import pulp


with open('d10.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
#print(inputs)

def extract(s):
    m = 0
    s = s[1:-1]
    N = len(s)
    for i in range(N):
        if s[i] == '#':
            
            m |= (1 << i)
            
            
    #$print(N, s, m)
    return m
    
def getMin(target, data):
    N = len(target)
    need = extract(target)
    #print(need)
    c = set()
    c.add(0)
    st = deque([0])
    step = 0
    
    while st:
        for _ in range(len(st)):
            cur = st.popleft()
            if cur == need:
                return step
            
            for i in data:
                nm = cur
                for j in i:
                    nm ^= (1 << j)
                
                #print(nm, i)
                if nm not in c:
                    c.add(nm)
                    st.append(nm)
        step += 1
    return -1
        
REQ = []
PRESSES = []
# process every data for runtime
for i in inputs:
    i = i.split()
    goal = i[0]
    data = i[1:]
    
    buttons = []
    for i in data:
        button = [int(j) for j in i[1:-1].split(',')]
        buttons.append(button)
        
    REQ.append((goal, buttons[:-1]))
    PRESSES.append(buttons[-1])
    
    


def part1():
    p1 = 0
    for target, conf in REQ:
        
        step = getMin(target, conf)
        print(target, conf, step)
        p1 += step

    print(p1)
    return p1

#$print(REQ)
print(PRESSES)

'''
can you apply the same technique to the same problem?
Increasing a counter for 400 seems to be too slow and the defining state would be too complicated and how do you define such state? 
2 ^ i + 4 ^ i ???.. too much

'''
def part2():
    
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
        
            
            
        
        
    p2 = 0
    for i in range(len(REQ)):
        goal = PRESSES[i]
        buttons = REQ[i][1]
        cnt = getMin(goal, buttons)
        p2 += cnt
    
    #print(p2)
    return p2
        

part2()