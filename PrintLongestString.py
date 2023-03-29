input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

# 1 method

c = input.split(" ")
print(c)
print(max(c, key=len))

# 2
length = 0
string = ""
for i in c:
    if len(i) > length:
        length=len(i)
        string = i
print(string)
