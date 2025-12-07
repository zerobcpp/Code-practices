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

from collections import defaultdict
c = defaultdict()

with open('d4.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
inputs = convert_list(inputs, toInt = False)

N = len(inputs)
M = len(inputs[0])
print(N, M)

def part1():
    res = 0
    rmv = False
    for i in range(N):
        for j in range(M):
            cnt = 0
            if inputs[i][j] == '@':
                for x, y in d8(i, j):
                    if 0 <= x < N and 0 <= y < M and inputs[x][y] == '@':
                        cnt += 1
                if cnt < 4:
                    res += 1
                    inputs[i][j] = '.'
                    rmv = True
    
    return res, rmv

def part2(rmv):
    res = 0
    while rmv:
        rmv = False
        for i in range(N):
            for j in range(M):
                cnt = 0
                if inputs[i][j] == '@':
                    for x, y in d8(i, j):
                        if 0 <= x < N and 0 <= y < M and inputs[x][y] == '@':
                            cnt += 1
                    if cnt < 4:
                        inputs[i][j] = '.'
                        rmv = True
                        res += 1
    
    return res
                        
                        
                        
    

p1, remove = part1() 
p2 = part2(remove)

print(p1, p1 + p2)


