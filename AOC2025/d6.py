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
from functools import reduce
c = defaultdict(list)

with open('d6.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
N = len(inputs)
M = len(inputs[0].split())

def part1():
    for i in range(N-1):
        row = inputs[i].split()
        for j in range(len(row)):
            c[j].append(int(row[j]))

    print(c)
    p1 = 0
    x = 0
    cmd = inputs[-1].split()

    for i in range(M):
        ops = cmd[i]
        if ops == '+':
            x = sum(c[i])
        elif ops == '*':
            x = reduce(lambda a, b: a*b , c[i], 1)
        
        #print(x, c[i], i, ops)
        p1 += x
    return p1

def part2():
    p2 = 0
    data = inputs
    #print(*data, sep ='\n')
    
    M = len(max(data, key=len))
    c = [0] * M
    #print(M)
    res = []
    temp = [] 
    for j in range(M-1, -1, -1):
        s = 0
        for i in range(N-1):
            if data[i][j] != ' ':
                s *= 10
                s += int(data[i][j]) if data[i][j] != ' ' else 0
            
        if s != 0:
            temp.append(s)
        else:
            res.append(temp[:])
            temp = []
    
    res.append(temp[:])
    res = res[::-1]
    cmd = inputs[-1].split()
    
    print(res, cmd)
    for i in range(len(cmd)):
        ops = cmd[i]
        x = 0
        if ops == '+':
            x = sum(res[i])
        elif ops == '*':
            x = reduce(lambda a, b: a*b , res[i], 1)
        
        print(x, res[i], i, ops)
        p2 += x
    
    return p2
    
        
#part1()
print(part2())