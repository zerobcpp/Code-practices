inputs = [3,2,4]
target = 6

combination = []
def combi(list, target):
    for i in range(len(inputs)):
        for j in range(i+1,len(inputs)):
            if inputs[i] + inputs[j] == target:
                return [i, j]

print(combi(inputs,target))