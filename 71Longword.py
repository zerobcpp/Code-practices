n = int(input())
words = []

for i in range(n):
    s = input()
    words.append(s)

for word in words:
    if word.isdigit():
        pass
    else:
        if len(word) > 10:
            print("%s%s%s" % (word[0], len(word)-2,word[-1]))
        else:
            print("%s" % word)
