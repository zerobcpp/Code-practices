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



with open('d20.txt', 'r+') as f:
    inputs = f.read()

from collections import defaultdict
inputs = inputs.split('\n')
convert_list(inputs)
#print(inputs)

G = inputs
N = len(inputs)
M = len(inputs[0])
start = None
end = None
cost = defaultdict(lambda: float('inf'))
for i in range(N):
    for j in range(M):
        if G[i][j] == 'S':
            start = (i, j)
            G[i][j] = '.'
        elif G[i][j] == 'E':
            end = (i, j)
            G[i][j] = '.'
    
    if start and end:
        break


print(start, end)
def p1():
    st = [(start[0], start[1], 0)]
    cc = []
    tot = 0
    seen = set(st)
    cheated = set()
    

    def start_cheat(i, j, new_i, new_j, seen, cost):
        if new_i < 0 or new_i >= N or new_j <  0 or new_j >= M or G[new_i][new_j] == '#':
            return
        
        #print(new_i, new_j, cost + 2)
        st = [(new_i, new_j, cost + 2)]
        while st:
            x, y, cost = st.pop()
            if (x, y) == end:
                
                cc.append(cost)
                return
            
            for k in range(4):
                dx, dy = d4[k] + x, d4[k+1] + y
                
                if G[dx][dy] != '#' and (dx, dy) not in seen:
                    seen.add((dx, dy))
                    st.append((dx, dy, cost + 1))
            

    while st:
        x, y, cost = st.pop()
        if (x, y) == end:
            tot = cost
            
        
        for k in range(4):
            dx, dy = d4[k] + x, d4[k+1] + y
        
            if G[dx][dy] == '#' and (dx, dy) not in cheated:
                cdx = dx + d4[k]
                cdy = dy + d4[k+1]
                start_cheat(x, y, cdx, cdy, seen.copy(), cost)
                cheated.add((dx, dy))
                
            if G[dx][dy] != '#' and (dx, dy) not in seen:
                st.append((dx, dy, cost+1))
                seen.add((dx, dy))
            
    print(cc, tot)
    p1 = 0
    for i in range(len(cc)):
        cc[i] -= tot
        p1 += 1 if abs(cc[i]) >= 100 else 0
    
    cc.sort()
    print(cc)

#1487 wrong
#1485 correct

from collections import deque
from collections import Counter

def p2():

    st = deque([(start[0], start[1], 0)])
    cc = []
    tot = 0
    seen = set([(start[0], start[1])])
    
    print(start, end)
    dist = defaultdict(int)
    dist[start[0], start[1]] = 0
    
    while st:
        x, y, cost = st.pop()
        if (x, y) == end:
            tot = cost
        
        for k in range(4):
            dx, dy = d4[k] + x, d4[k+1] + y
            if G[dx][dy] != '#' and (dx, dy) not in seen:
                dist[dx, dy] = cost + 1
                st.append((dx, dy, cost+1))
                seen.add((dx, dy))
                
        
    def start_cheat():
        tot = 0
        for i in range(N):
            for j in range(M):         
                if G[i][j] != '#':
                    cost = dist[i, j]
                    for dx in range(-20, 21):
                        nx = i + dx
                        if nx not in range(N):
                            continue
                        for dy in range(-20 + abs(dx), 21 - abs(dx)):
                            ny = j + dy
                            if ny not in range(M):
                                continue
                            if G[nx][ny] == '#':
                                continue
                            saving = dist[nx, ny] - dist[i, j] - (abs(dx) + abs(dy))
                            
                            if saving >= 100:
                                tot += 1
        return tot

                
    p2 = 0       
    p2 += start_cheat()
    print(p2)


#p1()
p2()