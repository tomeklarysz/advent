f = open(r"C:\Users\tomek\Documents\VscodeProjects\advent\1\text.txt", "r")
list = []
sum = 0
for x in f:
    temp = []
    for y in x:
        if y.isdigit():
            temp.append(int(y))
    sum += (temp[0]*10 + temp[-1])
print(sum)
f.close()