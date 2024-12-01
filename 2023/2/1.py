f = open("2/input.txt", "r")

# 12 red, 13 green, 14 blue
# there are 100 games
sum = 0
index = 1
for i in f:
    text = ""
    text = i.replace("Game ", "")
    text = text.split(";")
    if index == 100: text[0] = text[0][4:]
    else: text[0] = text[0][3:]
    done = False
    print(index)
    index += 1
    print(text)
    for x in text:
        x = x.split(",")
        print(x)
        for y in x:
            if done == True: break
            y = y.split()
            print(y)
            if int(y[0]) > 12:
                if y[1] == 'red':
                    done = True
                    break
                elif y[1] == 'green' and int(y[0]) > 13:
                    done = True
                    break
                elif y[1] == 'blue' and int(y[0]) > 14:
                    done = True
                    break
        if done == True: break
    if done == True: continue
    sum += index-1
    print("sum: "+str(sum))


print(sum)
f.close()