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
    0: [-1, 0], #^
    1: [0, 1],  #>
    2: [1, 0],  #v
    3: [0, -1], #<
}


with open('d13.txt', 'r+') as f:
    inputs = f.read()


inputs = inputs.split('\n')

N = len(inputs)
    
from functools import cache
import numpy as np

def p1():
    
    @cache
    def helper(i, j, x, y, A, B):
        if i > x or j > y:
            return float('inf')
        if i == x and j == y:
            return 0
        
        a = helper(i+A[0], j + A[1], x, y, A, B) + 3
        b = helper(i+B[0], j + B[1], x, y, A, B) + 1
        
        return min(a,b)


    p1 = 0
    for i in range(0, N, 4):
        A = inputs[i].split()
        B = inputs[i+1].split()
        Prize = inputs[i+2].split()

        Ax, Ay = int(A[2][2:-1]), int(A[3][2:])
        Bx, By = int(B[2][2:-1]), int(B[3][2:])
        Px, Py = int(Prize[1][2:-1]), int(Prize[2][2:])
        
        
        #print(a, b, p)
        cur = helper(0, 0, Px, Py, (Ax, Ay), (Bx, By))
        if cur != float('inf'):
            p1 += cur
    print(p1)



def p2():
    
    p2 = 0
    for i in range(0, N, 4):
        A = inputs[i].split()
        B = inputs[i+1].split()
        Prize = inputs[i+2].split()

        Ax, Ay = int(A[2][2:-1]), int(A[3][2:])
        Bx, By = int(B[2][2:-1]), int(B[3][2:])
        Px, Py = int(Prize[1][2:-1]), int(Prize[2][2:])
        Px += 10000000000000
        Py += 10000000000000
        arr = np.array([[Ax, Bx], [Ay, By]])
        x = np.array([Px, Py])
        
        result = (np.linalg.solve(arr, x))
        #print(result)
        result = np.round(result)
        #print(result)
        if result[0] * Ax + result[1] * Bx == Px and result[0] * Ay + result[1] * By == Py:
            p2 += result[0] * 3 + result[1]
            
            
        
    print(p2)
        
        

p2()



# 82754669444206 low