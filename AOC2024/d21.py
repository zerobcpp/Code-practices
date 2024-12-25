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
rd = {
    0 : '<',
    1 : '^',
    2 : '>', 
    3 : 'v', 
}

from collections import defaultdict, deque 
import heapq 
import math 
import itertools
with open('d21.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

door = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'], 
    ['.', '0', 'A'],
]
dirs = [
    ['.', '^', 'A'], 
    ['<', 'v', '>'],
]




   
def makeKeys(arr):
    N = len(arr)
    M = len(arr[0])    
    
    def dijkstra(start, end):
        st = ([(0, start, [])])
        dcost = defaultdict(lambda:float('inf'))
        while st:
            cost, cur, pressed = heapq.heappop(st)
            x, y = cur
            if cur == end:
                return (cost, sorted(pressed))
            
            for k in range(4):
                button = rd[k]
                dx, dy = x + d4[k], y + d4[k+1]
                nd = len(pressed) + 1
                if 0 <= dx < N and 0 <= dy < M and arr[dx][dy] != '.':
                    if nd < dcost[dx, dy]:
                        dcost[dx, dy] = nd
                        st.append((nd, (dx, dy), pressed + [button]))
                        

    cost = defaultdict(lambda :float('inf'))
    for i in range(N):
        for j in range(M):
            start = (i, j)
            ok = arr[i][j]
            if ok == '.':
                continue
            cost[ok, ok] = (0, [])
            
            for k in range(N):
                for l in range(M):
                    end = (k, l)
                    ik = arr[k][l]
                    if ik == '.':
                        continue
                    cost[ok, ik] = dijkstra(start, end)
    
    return cost
    
def convertKey(buttons, human = False):
    if human:
        c = cp
    else:
        c = cdr
    
    N = len(buttons)
    res = []
    prev = None
    
    for i in range(N):
        if not prev:
            prev = 'A'
        else:
            prev = buttons[i-1]
        cur = buttons[i]
    
        res.extend(c[prev, cur][1])
        
        res.extend('A')
        
    
    return res

cp = makeKeys(door)
cdr = makeKeys(dirs)
#print(cp['9', '7'])
#print(cp['7', '9'])

    
p1 = 0
for i in inputs:
    a = convertKey(i, True)
    
    b = convertKey(a)
    c = convertKey(b)
    print(''.join(a))
    print(''.join(b))
    print(''.join(c))
    num = int(''.join(filter(lambda x: x.isdigit(), i)))
    print(num, len(c))
    # p1 += num * len(c)
    # print(i)
    

#print(p1)


#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<A<AA^>>A<Av>AA^Av<<A^>>AvA^Av<<A^>>AAv<A>A^A<A>Av<A<A^>>AAA<Av>A^A

