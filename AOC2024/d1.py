
with open("d1.txt", "r+") as f:
    inputs = f.read()

inputs = inputs.split('\n')

left = []
right = []
rightc = {}
for i in inputs:
    l, r = i.split()
    l, r = int(l), int(r)
    left.append(int(l))
    right.append(int(r))
    rightc[r] = rightc.get(r, 0) + 1


dist = 0
left.sort()
right.sort()

N = len(left)
p2 = 0
p1 = 0

for i in range(N):
    l, r = left[i], right[i]

    p1 += abs(l - r)
    p2 += (l * rightc.get(l, 0))



print(p1, p2)