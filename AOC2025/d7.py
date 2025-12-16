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


with open('d7.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
inputs = convert_list(inputs)

#7print(*inputs, sep = '\n')
N = len(inputs)
M = len(inputs[0])

START = (0, inputs[0].index('S'))


def part1():
    st = [START]
    grid = inputs
    cnt = 0
    splitted = set()
    splitter = 0
    while st:
        x, y = st.pop()
        
        
        # check straight bottom for ^
        if (x+1) < N and grid[x+1][y] == '^':
            if (x+1, y) not in splitted:
                cnt += 1
                for dx, dy in ((x+1, y-1), (x+1, y+1)):
                    if 0 <= dx < N and 0 <= dy < M:
                        st.append((dx, dy))
                        grid[dx][dy] = '|'
                splitted.add((x+1, y))        
        else:
            dx = x + 1
            if 0 <= dx < N:
                st.append((dx, y))
                grid[dx][y] = '|'
        
        #print(len(st))
        
    #print(*grid, sep = '\n')
    print(cnt)
    return cnt


def part2():
    st = START
    
    cache = {}
    def helper(i, j):
        if i >= N:
            return 1
        if j < 0 or j >= M:
            return 0
        if (i, j) in cache:
            return cache[i, j]
        down = helper(i+1, j)
        left = right = 0 
        if inputs[i][j] == '^':
            left = helper(i, j-1)
            right = helper(i, j+1)
            cache[i, j] = left + right
            return left + right
        cache[i, j] = down
        return down

    
        return helper(st)
    res = helper(*st)
    print(len(cache), N, M)
    print(res)
    return res
        

#1762 too high
#part1()

part2() 

# part1 = bfs/dfs
# part2 = dp 
        
    
    

