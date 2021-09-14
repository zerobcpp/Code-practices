# This question is manhattan distance by disguise
from math import ceil

i1 = [int(i) for i in input().split(" ")]
i2 = [int(i) for i in input().split(" ")]
i3 = [int(i) for i in input().split(" ")]
i4 = [int(i) for i in input().split(" ")]
i5 = [int(i) for i in input().split(" ")]

matrix = [i1, i2, i3, i4, i5]

index = 1
found = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            found = index
        index += 1

# y distance to adjust
y = abs(ceil(found / 5) - ceil(13 / 5))
# x distance to adjust
x = found % 5
# occasion when x is the last index of the row
if x == 0:
    x = 1
x = abs(3 - x)
print(x + y)
