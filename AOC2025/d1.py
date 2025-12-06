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

with open('d1.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')
#print(inputs)
start = 50

prev = inputs[0][0]
p1 = 0
p2 = 0
for i in inputs:
    
    D = i[0]
    R = int(i[1:])
    zero = 0
    
    last = start
    if D == 'L':
        back = 0
        if start > 0:
            back = 100 - start
        zero += (back + R) // 100
        start -= R
        

    else:
        start += R
        zero += start // 100
    #print(abs(last//100-start//100), R, start % 100)
    
    start %= 100
    if start == 0:
        p1 += 1
    
    p2 += zero
    print(i, start, zero, p1, p2)



print(p1, p2, p2-p1)
    
   
    




#5949, too low     
#5956, too low
#5969, too high