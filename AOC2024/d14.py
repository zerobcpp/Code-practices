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



with open('d14.txt', 'r+') as f:
    inputs = f.read()




inputs = inputs.split('\n')
N = 103
M = 101
grid = [[0] * M for _ in range(N)]
def p1():
    bots = []
    for i, v in enumerate(inputs):
        p, v = v.split()
        
        p = p.split(',')
        v = v.split(',')
        y,x = int(p[0][2:]), int(p[1])
        dy,dx = int(v[0][2:]), int(v[1])
        
        
        
        #print(x, y, dx, dy)
        px = py = 0 
        px = ( 100 * dx + x) % N
        py = ( 100 * dy + y) % M
        
        #bots[i] = [px, py, dx, dy]
        bots.append((px, py, i))
        grid[px][py] += 1

    xmid = N // 2
    ymid = M // 2
        
    res = [0, 0, 0, 0]

    for x, y, i in bots:
        if x == xmid or y == ymid:
            continue
        
        if x < xmid and y < ymid:
            res[0] += 1
        elif x < xmid and y > ymid:
            res[1] += 1
        elif x > xmid and y < ymid:
            res[2] += 1
        elif x > xmid and y > ymid:
            res[3] += 1
    
    
    for i in grid:
        print(i)
    print(res)
    p1 = 1
    for i in res:
        p1 *= i
    print(len(bots))
    print(p1)

    # 87904138 low
    # 221835159 high


def p2():
    bots = []    
    xmid = N // 2
    ymid = M // 2
    prev = 0
    for i, v in enumerate(inputs):
        p, v = v.split()
        
        p = p.split(',')
        v = v.split(',')
        y,x = int(p[0][2:]), int(p[1])
        dy,dx = int(v[0][2:]), int(v[1])
        
        #print(x, y, dx, dy)
        #bots[i] = [px, py, dx, dy]
        bots.append((x, y, dx, dy))
    
    def verify(grid):
        xcnt = 0
        ycnt = 0
        nonlocal prev
        def pr():
            for i in grid:
                for j in i:
                    if j == 0:
                        print('.', end = ' ')
                    else:
                        print(j, end=' ')
                print()
        
        mx = 0
        for i in grid:
            cur = 0
            for j in i:
                if j != 0:
                    cur += 1
            mx = max(cur, mx)
        
        if mx > prev:
            prev = max(prev, mx)
            print(prev, mx)
            pr()
        
        # for i in range(N):
        #     if grid[i][ymid] > 0:
        #         xcnt += 1
        #     if grid[i][ymid-1] > 0:
        #         xcnt += 1
        #     if grid[i][ymid+1] > 0:
        #         xcnt += 1
        
        # for i in range(M):
        #     if grid[xmid][i] > 0:
        #         ycnt += 1
        #     if grid[xmid-1][i] > 0:
        #         ycnt += 1
        #     if grid[xmid+1][i] > 0:
        #         ycnt += 1
        
        # print(xcnt, ycnt)
        

            
        
    
    def run(seconds):
        grid = [[0] * M for _ in range(N)]
        for x, y, dx, dy in bots:
            px = py = 0 
            px = (seconds* dx + x) % N
            py = (seconds* dy + y) % M
            grid[px][py] += 1
        
        verify(grid)
    import time
    i = 1000
    while True:
        run(i)
        i += 1
        print(i)
       

p1()
#p2()