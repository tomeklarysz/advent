f = open("2/input.txt", "r")


sum = 0
index = 1
for i in f:
    text = ""
    text = i.replace("Game ", "")
    text = text.split(";")
    dictionary = {'red': 0, 'blue': 0, 'green': 0}
    if index == 100: text[0] = text[0][4:]
    else: text[0] = text[0][3:]
    # done = False
    print()
    index += 1
    print(text)
    for x in text:
        x = x.split(",")
        print(x)
        for y in x:
            y = y.split()
            if (int(y[0])>dictionary[y[1]]):
                dictionary.update({y[1]: int(y[0])})
            # print(y)
    # sum += index-1
    # print("sum: "+str(sum))
    print(dictionary)
    power = 1
    for val in dictionary.values():
        power *= val
    print("Power: "+str(power))
    sum += power

print(sum)
f.close()