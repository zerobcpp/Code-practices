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



with open('d18.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

    
from collections import defaultdict
N = 71
M = 71


grid = [['.'] * M for _ in range(N)]



def p1():
    for i in inputs[:1024]:

        x, y = list(int(i) for i in i.split(','))
        grid[x][y] = '#'
        

    cost = defaultdict(lambda: float('inf'))
    cost[0, 0] = 0
    start = [(0, 0)]
    for i in grid:
        print(i)
    while start:
        x, y = start.pop()
        
        for k in range(4):
            dx, dy = x + d4[k], y + d4[k+1]
            nw = cost[x, y] + 1
            if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] != '#':
                if cost[dx, dy] > nw:
                    cost[dx, dy] = nw
                    start.append((dx, dy))
                    
    print(cost[N-1, M-1])



def p2():
    
    def mark(idx):
        i = inputs[idx]
        x, y = list(int(i) for i in i.split(','))
        grid[x][y] = '#'
    
    
    def helper():
        cost = defaultdict(lambda: float('inf'))
        cost[0, 0] = 0
        start = [(0, 0)]
        seen = set(start)
        while start:
            x, y = start.pop()
            for k in range(4):
                dx, dy = x + d4[k], y + d4[k+1]
                nw = cost[x, y] + 1
                if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] != '#' and (dx, dy) not in seen:
                    if cost[dx, dy] > nw:
                        cost[dx, dy] = nw
                        start.append((dx, dy))
                        seen.add((dx, dy))
        
        return (N-1, M-1) in cost
        
    for i in range(len(inputs)):
        mark(i)
        print(i)
        if not helper():
            print(inputs[i])
            break
    
    
p2()
