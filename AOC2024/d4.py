with open('d4.txt', 'r+') as f:
    inputs = f.read()

inputs = inputs.split('\n')

#print(inputs)

N = len(inputs)
M = len(inputs[0])

st = []
word = "XMAS"

dirs = [
    [0, 1], 
    [0, -1], 
    [-1, 0],
    [1, 0], 
    [-1, 1], 
    [-1, -1],
    [1, -1],
    [1, 1],
]

# dirs = {'up' :   [0, 1], 
#         'down':  [0, -1], 
#         'left':  [-1, 0],
#         'right': [1, 0], 
#         'nw':    [-1, 1], 
#         'sw':    [-1, -1], 
#         'se':    [1, -1],
#         'nw':    [1, 1],
#         }

# kdirs = {}

# for k, v in dirs.items():
#     kdirs[tuple(v)] = k



for i in range(N):
    for j in range(M):
        if inputs[i][j] == 'X':
            st.append((i, j, 0))


p1 = 0
def helper(cur):
    x, y, step = cur
    cnt = 0
    for direction in dirs:
        st = [(x, y, step)]
        
        
        while st:
            ix, iy, istep = st.pop()
            if istep == 3:
                print(x, y,  direction)
                cnt += 1
                continue

            dx, dy = ix + direction[0], iy + direction[1]
            if 0 <= dx < N and 0 <= dy < M:
                if inputs[dx][dy] == word[istep+1]:
                    st.append((dx, dy, istep + 1))
            
    return cnt

def part1():
    for i in st:
        p1 += helper(i)
    print(p1)


p2 = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        diag = inputs[i-1][j-1] + inputs[i][j] + inputs[i + 1][j+1]
        adiag = inputs[i+1][j-1] + inputs[i][j] + inputs[i-1][j+1]
        p2 += (diag in ["MAS", "SAM"]) and (adiag in ["MAS", "SAM"])
            

print(p2)



#2035 too high
#1919 too low