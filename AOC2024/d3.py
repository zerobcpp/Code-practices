with open('d3.txt', 'r+') as f:
    inputs = f.read()

#inputs = inputs.split('\n')


import re
# print(inputs)
# print(len(inputs))

def part1():
    pattern = r"mul\((\d+),(\d+)\)"
    find = re.findall(pattern, inputs)
    print(find)
    p1 = 0

    for i in find:
        x, y = int(i[0]), int(i[1])
        p1 += (x * y)

    print(p1)


p2pattern = r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)"
find = re.findall(p2pattern, inputs)
p2 = 0

mode = True
for i in find:
    flag, a, b = i[0], i[1], i[2]
    if flag and flag == ("don't()"):
        mode = False
    if flag and flag == ("do()"):
        mode = True
    
    if not flag:
        if mode:
            a, b = int(a), int(b)
            p2 += (a * b)
    
    
print(p2)