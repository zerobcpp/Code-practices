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

with open('d25.txt', 'r+') as f:
    inputs = f.read()

top = []
down = []
inputs = inputs.split('\n\n')



for i in inputs:
    
    i = i.split('\n')

    
    if '#' in i[0]:
        top.append(i)
    if '#' in i[-1]:
        down.append(i)


keyUp = []
keyDown = []
for i in top:
    N = len(i)
    M = len(i[0])
    
    
    seq = []
    for j in range(M):
        cnt = -1
        for k in range(N):
            if i[k][j] == '#':
                cnt += 1
            else:
                break
        seq.append(cnt)
    
    keyUp.append(seq)
    

for i in down:
    N = len(i)
    M = len(i[0])
    seq = []
    for j in range(M):
        cnt = -1
        for k in range(N-1, -1, -1):
            if i[k][j] == '#':
                cnt += 1
            else:
                break
        seq.append(cnt)
    keyDown.append(seq)
                
p1 = 0
def check(up, down):
    N = len(up)
    for i in range(N):
        if up[i] + down[i] >= 6:
            return False
    
    return True

for i in keyUp:
    for j in keyDown:
        if check(i, j):
            p1 += 1

print(p1)
     
    